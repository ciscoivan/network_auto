import logging
from starlette.applications import Starlette
from starlette.responses import StreamingResponse
from starlette.routing import Route
import uvicorn
import asyncio

# 配置详细日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('direct_sse')

# 简单的SSE端点
async def sse_endpoint(request):
    logger.info("SSE connection established")
    
    async def event_generator():
        # 发送初始事件
        yield f"data: {{\"message\": \"Hello from SSE!\"}}\n\n"
        
        # 每2秒发送一次心跳
        for i in range(5):
            await asyncio.sleep(2)
            yield f"data: {{\"message\": \"Heartbeat {i}\"}}\n\n"
        
        # 发送结束事件
        yield f"data: {{\"message\": \"Connection closing\"}}\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )

# 创建Starlette应用
app = Starlette(
    debug=True,
    routes=[
        Route("/sse", endpoint=sse_endpoint),
    ]
)

if __name__ == "__main__":
    logger.info("Starting direct SSE server...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="debug"
    )
