from flask import Flask, request, jsonify, render_template_string
import netmiko
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import SSHException
import csv
import threading
import queue
import os

app = Flask(__name__)

def get_devices():
    devices = []
    try:
        with open('devices.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                devices.append(row)
    except FileNotFoundError:
        print("devices.csv 文件未找到。")
    return devices

def get_inspection_commands():
    commands = []
    try:
        with open('inspection_commands.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                command = row[0]
                # 跳过内容为 # 的命令
                if command.strip() != '#':
                    commands.append(command)
    except FileNotFoundError:
        print("inspection_commands.csv 文件未找到。")
    return commands

def get_config_commands():
    commands = []
    try:
        with open('config_commands.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                commands.append(row[0])
    except FileNotFoundError:
        print("config_commands.csv 文件未找到。")
    return commands

def connect_to_device(q, results):
    while True:
        device = q.get()
        if device is None:
            break
        ip = device[0]
        username = device[1]
        password = device[2]
        device_type = device[3]
        inspection_output = ''
        config_output = ''
        login_status = ''

        inspection_commands = get_inspection_commands()
        config_commands = get_config_commands()

        try:
            net_connect = ConnectHandler(device_type=device_type, ip=ip, username=username, password=password)
            login_status = f'<p class="success">设备 {ip} 登录成功</p>'  # 新增登录成功显示

            # 执行巡检命令
            inspection_output = '<h4>巡检命令执行结果</h4>'
            for command in inspection_commands:
                inspection_output += f'<p><strong>设备 IP: {ip}, 执行巡检命令: {command}</strong></p>'
                output = net_connect.send_command(command)
                inspection_output += f'<pre class="command-output">{output}</pre>'

            # 执行配置命令
            config_output = '<h4>配置命令执行结果</h4>'
            if config_commands:
                for command in config_commands:
                    config_output += f'<p><strong>设备 IP: {ip}, 执行配置命令: {command}</strong></p>'
                output = net_connect.send_config_set(config_commands)
                config_output += f'<pre class="command-output">{output}</pre>'

            net_connect.disconnect()
            output = login_status + inspection_output + config_output  # 合并登录状态和执行结果
            results[ip] = output

            with open(f'{ip}.txt', 'w') as f:
                f.write(output.replace('<h4>', '').replace('</h4>', '').replace('<p>', '').replace('</p>', '').replace('<pre class="command-output">', '').replace('</pre>', ''))

        except NetMikoTimeoutException:
            results[ip] = f'<p class="error">设备 {ip} 不可达</p>'
        except AuthenticationException:
            results[ip] = f'<p class="error">设备 {ip} 认证失败</p>'
        except SSHException:
            results[ip] = f'<p class="error">设备 {ip} SSH 问题。请确保 SSH 已启用。</p>'
        q.task_done()

@app.route('/', methods=['GET'])
def index():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>执行命令</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <style>
            body {
                background: linear-gradient(135deg, #f4f4f9, #e0e0e9);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .container {
                margin-top: 10vh;
                background-color: #ffffff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #0d6efd;
                font-weight: 600;
                margin-bottom: 30px;
            }
            .btn {
                font-size: 1.2rem;
                padding: 12px 30px;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <div class="container text-center">
            <h1>ivan网络自动化巡检工具</h1>
            <p class="lead">轻松执行网络设备的巡检和配置命令。</p>
            <form action="/execute_commands" method="get">
                <button type="submit" class="btn btn-lg btn-primary">下发巡检命令</button>
            </form>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/execute_commands', methods=['GET'])
def execute_commands():
    q = queue.Queue()
    devices = get_devices()
    results = {}

    num_threads = 5
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=connect_to_device, args=(q, results))
        t.daemon = True
        t.start()
        threads.append(t)

    for device in devices:
        q.put(device)

    q.join()

    for _ in range(num_threads):
        q.put(None)
    for t in threads:
        t.join()

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>执行结果</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <style>
            body {
                background-color: #f4f4f9;
            }
            .container {
                margin-top: 5vh;
            }
            table {
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            th {
                background-color: #0d6efd;
                color: white;
            }
            pre.command-output {
                background-color: #e9ecef;
                padding: 10px;
                border-radius: 5px;
                white-space: pre-wrap;
                margin-bottom: 15px;
            }
            p.error {
                color: red;
            }
            p.success {
                color: green;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="text-center text-primary mb-4">执行结果</h1>
            <div class="d-flex justify-content-center mb-3">
                <div class="spinner-border text-primary" role="status" id="loading-spinner" style="display: none;">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
            <table class="table table-striped table-bordered">
                <thead>
                    <tr>
                        <th>设备 IP</th>
                        <th>巡检命令</th>
                        <th>配置命令</th>
                        <th>执行结果</th>
                    </tr>
                </thead>
                <tbody>
    """
    inspection_commands = get_inspection_commands()
    config_commands = get_config_commands()
    for ip, output in results.items():
        inspection_commands_str = "<br>".join(inspection_commands)
        config_commands_str = "<br>".join(config_commands)
        html += f"""
                    <tr>
                        <td>{ip}</td>
                        <td>{inspection_commands_str}</td>
                        <td>{config_commands_str}</td>
                        <td>{output}</td>
                    </tr>
        """
    html += """
            </tbody>
            </table>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const spinner = document.getElementById('loading-spinner');
                spinner.style.display = 'none';
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)