"""
远程服务入口
"""
from config import cfg
from internal.grpc import run_server
from internal.core.mlog import logger

def main() -> None:
    server, port = run_server(cfg.get("app", "port"))
    print(f"server run on {cfg.get('app', 'addr') + ':' + str(port)}")
    logger.info(f"server run on: {port}")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        logger.info("server stopping...")
        print("server stopping...")


if __name__ == "__main__":
    main()
