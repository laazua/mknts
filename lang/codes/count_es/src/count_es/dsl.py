"""
date: 2024-01-05
"""
import enum


# week count
WEEK_CNT = {
  "query": {
    "bool": {
      "must": [
        {
          "wildcard": {
            "server_name.keyword": "*.xxxx.com"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": "now-6d/d",
              "lte": "now/d"
            }
          }
        }
      ],
      "must_not": [
        {
          "terms": {
            "server_name": [
              "help.xxxx.com",
              "hl.xxxx.com"
            ]
          }
        }
      ]
    }
  },
  "size": 0,
  "track_total_hits": True,
  "aggs": {
    "server_name": {
      "terms": {
        "field": "server_name.keyword",
        "size": 100
      },
      "aggs": {
        "code": {
          "terms": {
            "field": "response_code.keyword",
            "size": 20
          },
          "aggs": {
            "path": {
              "terms": {
                "field": "path_2nd.keyword",
                "size": 20
              }
            }
          }
        },
        "city": {
          "terms": {
            "field": "geoip.city_name",
            "size": 20
          },
          "aggs": {
            "country_tag": {
              "top_hits": {
                "_source": {
                  "includes": [
                    "geoip.country_name",
                    "geoip.region_name"
                  ]
                },
                "size": 1
              }
            }
          }
        },
        "clientip": {
          "terms": {
            "field": "clientip",
            "size": 20
          },
          "aggs": {
            "country_tag": {
              "top_hits": {
                "_source": {
                  "includes": [
                    "geoip.country_name",
                    "geoip.region_name"
                  ]
                },
                "size": 1
              }
            }
          }
        },
        "path": {
          "terms": {
            "field": "path_2nd.keyword",
            "size": 20
          },
          "aggs": {
            "time": {
              "percentiles": {
                "field": "request_time",
                "percents": [90, 95, 99.9]
              }
            },
            "code": {
              "terms": {
                "field": "response_code.keyword",
                "size": 20
              }
            }
          }
        },
        "day": {
          "date_histogram": {
            "field": "@timestamp",
            "interval": "day",
            "format": "yyyy-MM-dd"
          }
        }
      }
    }
  }
}
# month count
MOUTH_CNT = {
  "query": {
    "bool": {
      "must": [
        {
          "wildcard": {
            "server_name.keyword": "*.xxxx.com"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": "now-1M/M",
              "lte": "now/M"
            }
          }
        }
      ],
      "must_not": [
        {
          "terms": {
            "server_name": [
              "zz.xxxx.com",
              "yy.xxxx.com"
            ]
          }
        }
      ]
    }
  },
  "size": 0,
  "track_total_hits": True,
  "aggs": {
    "server_name": {
      "terms": {
        "field": "server_name.keyword",
        "size": 100
      },
      "aggs": {
        "code": {
          "terms": {
            "field": "response_code.keyword",
            "size": 20
          },
          "aggs": {
            "path": {
              "terms": {
                "field": "path_2nd.keyword",
                "size": 20
              }
            }
          }
        },
        "city": {
          "terms": {
            "field": "geoip.city_name",
            "size": 20
          },
          "aggs": {
            "country_tag": {
              "top_hits": {
                "_source": {
                  "includes": [
                    "geoip.country_name",
                    "geoip.region_name"
                  ]
                },
                "size": 1
              }
            }
          }
        },
        "clientip": {
          "terms": {
            "field": "clientip",
            "size": 20
          },
          "aggs": {
            "country_tag": {
              "top_hits": {
                "_source": {
                  "includes": [
                    "geoip.country_name",
                    "geoip.region_name"
                  ]
                },
                "size": 1
              }
            }
          }
        },
        "path": {
          "terms": {
            "field": "path_2nd.keyword",
            "size": 20
          },
          "aggs": {
            "time": {
              "percentiles": {
                "field": "request_time",
                "percents": [90, 95, 99.9]
              }
            },
            "code": {
              "terms": {
                "field": "response_code.keyword",
                "size": 20
              }
            }
          }
        },
        "day": {
          "date_histogram": {
            "field": "@timestamp",
            "interval": "day",
            "format": "yyyy-MM-dd"
          }
        }
      }
    }
  }
}
# domain name and index map
IDX_MAP = {
    "xxxx": "access-www-xxxx",
    "zzzz": "access-www-zzzz",
    "yyyy": "access-www-yyyy",
    "oooo": "access-www-oooo",
    "mmmm": "access-www-mmmm",
    "aaaa": "access-www-aaaa",
    "bbbb": "access-www-bbbb",
    "cccc": "access-www-cccc",
    "dddd": "access-www-dddd",
    "eeee": "access-www-eeee",
    "ffff": "access-www-ffff",
    "gggg": "access-www-gggg",
}


TotalIndex = {
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  },
  "mappings": {
    "dynamic": False,
    "properties": {
      "domain": {
        "type": "keyword"
      },
      "count": {
        "type": "integer"
      },
      "code": {
        "type": "nested",
        "properties": {
          "200": {
            "type": "integer"
          },
          "402": {
            "type": "integer"
          },
          "400": {
            "type": "integer"
          }
        }
      }
    }
  }
}


@enum.unique
class CntType(enum.Enum):
    """cnt type"""
    Week = "week_cnt"
    Month = "month_cnt"


@enum.unique
class CntItem(enum.Enum):
    TotCnt = "totcnt"
    IpCnt = "ip"
    CityCnt = "city"
    CodeCnt = "code"
    PathCnt = "path"
