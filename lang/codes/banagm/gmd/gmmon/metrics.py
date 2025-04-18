# -*- coding: utf-8 -*-
"""metrics数据采集"""

import prometheus_client


class Monitor:
    def __init__(self) -> None:
        self.collector_registry = prometheus_client.CollectorRegistry(auto_describe=False)
        self.request_time_max_map = {}
        self.http_request_summary = prometheus_client.Summary(name="http_server_requests_seconds",
             documentation="Num of request time summary",
             labelnames=("method", "code", "uri"),
             registry=self.collector_registry)