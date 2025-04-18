import unittest

from src.count_es import xlsx


data = [
    {
        "key": "www.xxxx.com",
        "doc_count": 5556820,
        "path": {
            "doc_count_error_upper_bound": 563,
            "sum_other_doc_count": 336160,
            "buckets": [
                {
                    "key": "/r/search",
                    "doc_count": 2548706,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "404", "doc_count": 2548706}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.017999999225139618,
                            "95.0": 0.01899999938905239,
                            "99.0": 0.019999999552965164,
                        }
                    },
                },
                {
                    "key": "/help/question",
                    "doc_count": 2042584,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 2009273},
                            {"key": "302", "doc_count": 32242},
                            {"key": "400", "doc_count": 807},
                            {"key": "404", "doc_count": 146},
                            {"key": "499", "doc_count": 116},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.09557305743756717,
                            "95.0": 0.10400000214576721,
                            "99.0": 0.15010380608010593,
                        }
                    },
                },
                {
                    "key": "/Api/qyWap",
                    "doc_count": 297499,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 297455},
                            {"key": "400", "doc_count": 34},
                            {"key": "404", "doc_count": 7},
                            {"key": "499", "doc_count": 3},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.7185248192999032,
                            "95.0": 0.8501574885466987,
                            "99.0": 1.019992383883395,
                        }
                    },
                },
                {
                    "key": "/r/goods",
                    "doc_count": 83163,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "404", "doc_count": 83163}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.017999999225139618,
                            "95.0": 0.01899999938905239,
                            "99.0": 0.019999999552965164,
                        }
                    },
                },
                {
                    "key": "/Api/QyWapV2",
                    "doc_count": 36723,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 36647},
                            {"key": "499", "doc_count": 74},
                            {"key": "400", "doc_count": 2},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.27142567091934916,
                            "95.0": 0.3481023998856796,
                            "99.0": 0.46784624673426106,
                        }
                    },
                },
                {
                    "key": "/Api/qyWapV2",
                    "doc_count": 33721,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 33711},
                            {"key": "499", "doc_count": 8},
                            {"key": "400", "doc_count": 2},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.7226658438438694,
                            "95.0": 0.7517521202989986,
                            "99.0": 0.8169951941013338,
                        }
                    },
                },
                {
                    "key": "/ajax/show_static",
                    "doc_count": 25432,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 25397},
                            {"key": "499", "doc_count": 34},
                            {"key": "403", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.04100000113248825,
                            "95.0": 0.0430000014603138,
                            "99.0": 0.05400000140070915,
                        }
                    },
                },
                {
                    "key": "/user/PayQRCode",
                    "doc_count": 22553,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 22547},
                            {"key": "404", "doc_count": 3},
                            {"key": "499", "doc_count": 3},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.125,
                            "95.0": 0.13300000131130219,
                            "99.0": 0.1661566606660688,
                        }
                    },
                },
                {
                    "key": "/api/timing",
                    "doc_count": 11804,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 11791},
                            {"key": "404", "doc_count": 13},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.03999999910593033,
                            "95.0": 0.309783928309168,
                            "99.0": 0.32600000500679016,
                        }
                    },
                },
                {
                    "key": "/help/tm",
                    "doc_count": 9431,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "404", "doc_count": 9431}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.017999999225139618,
                            "95.0": 0.01899999938905239,
                            "99.0": 0.02039666628465073,
                        }
                    },
                },
                {
                    "key": "/api/DelayQueue",
                    "doc_count": 8816,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 8816}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07800000160932541,
                            "95.0": 0.08100000023841858,
                            "99.0": 0.0860000029206276,
                        }
                    },
                },
                {
                    "key": "/Api/qy_wap",
                    "doc_count": 5360,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 5358},
                            {"key": "400", "doc_count": 1},
                            {"key": "499", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.0729999989271164,
                            "95.0": 0.07599999755620956,
                            "99.0": 0.07999999821186066,
                        }
                    },
                },
                {
                    "key": "/index.php/api",
                    "doc_count": 5344,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 5325},
                            {"key": "302", "doc_count": 12},
                            {"key": "499", "doc_count": 6},
                            {"key": "404", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.08399999886751175,
                            "95.0": 0.35324443600795896,
                            "99.0": 1.090999960899353,
                        }
                    },
                },
                {
                    "key": "/Ajax/gethistory",
                    "doc_count": 4543,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 4543}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.03999999910593033,
                            "95.0": 0.04100000113248825,
                            "99.0": 0.04399999976158142,
                        }
                    },
                },
                {
                    "key": "/ajax/get_ajax_main_public_html",
                    "doc_count": 4342,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 4147},
                            {"key": "403", "doc_count": 122},
                            {"key": "499", "doc_count": 73},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.5563999831676485,
                            "95.0": 1.9085228334154396,
                            "99.0": 3.005080108642578,
                        }
                    },
                },
                {
                    "key": "/Api/WapContract",
                    "doc_count": 4174,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 4164},
                            {"key": "499", "doc_count": 10},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.14307500571012494,
                            "95.0": 0.14956000506877895,
                            "99.0": 0.1589999943971634,
                        }
                    },
                },
                {
                    "key": "/ajax/get_ajax_main_kefu_html",
                    "doc_count": 4004,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 3805},
                            {"key": "499", "doc_count": 199},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.3224833418925602,
                            "95.0": 0.6433000057935712,
                            "99.0": 1.1602199864387515,
                        }
                    },
                },
                {
                    "key": "/r/global-search",
                    "doc_count": 3846,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "404", "doc_count": 3846}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.01899999938905239,
                            "95.0": 0.01899999938905239,
                            "99.0": 0.019999999552965164,
                        }
                    },
                },
                {
                    "key": "/public/js",
                    "doc_count": 3720,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 3618},
                            {"key": "404", "doc_count": 69},
                            {"key": "304", "doc_count": 33},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.0,
                            "95.0": 0.0010000000474974513,
                            "99.0": 0.017000000923871994,
                        }
                    },
                },
                {
                    "key": "/api/ajax",
                    "doc_count": 2966,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 2957},
                            {"key": "499", "doc_count": 9},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.10499999672174454,
                            "95.0": 0.10999999940395355,
                            "99.0": 1.6920400238037154,
                        }
                    },
                },
            ],
        },
        "code": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "200",
                    "doc_count": 2819377,
                    "path": {
                        "doc_count_error_upper_bound": 321,
                        "sum_other_doc_count": 273213,
                        "buckets": [
                            {"key": "/help/question", "doc_count": 2009273},
                            {"key": "/Api/qyWap", "doc_count": 297455},
                            {"key": "/Api/QyWapV2", "doc_count": 36647},
                            {"key": "/Api/qyWapV2", "doc_count": 33711},
                            {"key": "/ajax/show_static", "doc_count": 25397},
                            {"key": "/user/PayQRCode", "doc_count": 22547},
                            {"key": "/api/timing", "doc_count": 11791},
                            {"key": "/api/DelayQueue", "doc_count": 8816},
                            {"key": "/Api/qy_wap", "doc_count": 5358},
                            {"key": "/index.php/api", "doc_count": 5325},
                            {"key": "/Ajax/gethistory", "doc_count": 4547},
                            {"key": "/Api/WapContract", "doc_count": 4164},
                            {
                                "key": "/ajax/get_ajax_main_public_html",
                                "doc_count": 4147,
                            },
                            {"key": "/ajax/get_ajax_main_kefu_html", "doc_count": 3805},
                            {"key": "/public/js", "doc_count": 3618},
                            {"key": "/api/ajax", "doc_count": 2957},
                            {"key": "/themes/simplebootx", "doc_count": 2199},
                            {"key": "/Api/QyWapBuryingPoint", "doc_count": 1934},
                            {"key": "/portal/send", "doc_count": 1764},
                            {"key": "/user/goods", "doc_count": 1739},
                        ],
                    },
                },
                {
                    "key": "404",
                    "doc_count": 2684007,
                    "path": {
                        "doc_count_error_upper_bound": 81,
                        "sum_other_doc_count": 29928,
                        "buckets": [
                            {"key": "/r/search", "doc_count": 2548706},
                            {"key": "/r/goods", "doc_count": 83163},
                            {"key": "/help/tm", "doc_count": 9431},
                            {"key": "/r/global-search", "doc_count": 3850},
                            {"key": "/r/g-goods", "doc_count": 1734},
                            {
                                "key": "/.well-known/apple-app-site-association",
                                "doc_count": 657,
                            },
                            {"key": "/r/cgoods", "doc_count": 647},
                            {"key": "/r/pgoods", "doc_count": 609},
                            {"key": "/help/mp", "doc_count": 584},
                            {"key": "/data/upload", "doc_count": 534},
                            {"key": "/ajax/getGoodsQyDetailEvent", "doc_count": 492},
                            {"key": "/httpswpa.qq.com/msgrd", "doc_count": 372},
                            {"key": "/m/consult", "doc_count": 306},
                            {"key": "/r/consulte", "doc_count": 300},
                            {"key": "/index.php/Ajax", "doc_count": 251},
                            {"key": "/css/modules", "doc_count": 216},
                            {"key": "/help/fuwu", "doc_count": 130},
                            {"key": "/help/question", "doc_count": 123},
                            {"key": "/s/oss", "doc_count": 114},
                            {"key": "/help/guwen", "doc_count": 69},
                        ],
                    },
                },
                {
                    "key": "302",
                    "doc_count": 34268,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 279,
                        "buckets": [
                            {"key": "/help/question", "doc_count": 32242},
                            {"key": "/user/ssq", "doc_count": 206},
                            {"key": "/user/goods", "doc_count": 200},
                            {"key": "/user/safety.html", "doc_count": 146},
                            {"key": "/api/oauth", "doc_count": 125},
                            {"key": "/mt/template", "doc_count": 114},
                            {"key": "/searchall/keyword", "doc_count": 93},
                            {"key": "/user/ticketSystem", "doc_count": 87},
                            {"key": "/user/login.html", "doc_count": 68},
                            {"key": "/Api/cart2", "doc_count": 59},
                            {"key": "/user/capital", "doc_count": 51},
                            {"key": "/user/message", "doc_count": 40},
                            {"key": "/user/order", "doc_count": 40},
                            {"key": "/mt/open.html", "doc_count": 31},
                            {"key": "/user/safety", "doc_count": 31},
                            {"key": "/user/need", "doc_count": 29},
                            {"key": "/user/index", "doc_count": 21},
                            {"key": "/mt/suppliers_enter.html", "doc_count": 18},
                            {"key": "/Api/Cart2", "doc_count": 17},
                            {"key": "/mt/transfer.html", "doc_count": 17},
                        ],
                    },
                },
                {
                    "key": "301",
                    "doc_count": 11581,
                    "path": {
                        "doc_count_error_upper_bound": 24,
                        "sum_other_doc_count": 11132,
                        "buckets": [
                            {"key": "/consult/3-14309.html", "doc_count": 52},
                            {"key": "/consult/3-190.html", "doc_count": 52},
                            {"key": "/consult/3-751.html", "doc_count": 40},
                            {"key": "/consult/3-18474.html", "doc_count": 36},
                            {"key": "/consult/3-105.html", "doc_count": 32},
                            {"key": "/consult/3-12.html", "doc_count": 32},
                            {"key": "/consult/3-188.html", "doc_count": 29},
                            {"key": "/consult/3-235.html", "doc_count": 25},
                            {"key": "/consult/3-40.html", "doc_count": 24},
                            {"key": "/consult/3-43.html", "doc_count": 24},
                            {"key": "/consult/3-7046.html", "doc_count": 19},
                            {"key": "/consult/3-1811.html", "doc_count": 17},
                            {"key": "/consult/3-4822.html", "doc_count": 14},
                            {"key": "/consult/3-4188.html", "doc_count": 13},
                            {"key": "/consult/3-3015.html", "doc_count": 9},
                            {"key": "/consult/3-839.html", "doc_count": 7},
                            {"key": "/consult/3-10508.html", "doc_count": 6},
                            {"key": "/consult/3-1826.html", "doc_count": 6},
                            {"key": "/consult/3-7636.html", "doc_count": 6},
                            {"key": "/consult/3-10046.html", "doc_count": 5},
                        ],
                    },
                },
                {
                    "key": "400",
                    "doc_count": 5684,
                    "path": {
                        "doc_count_error_upper_bound": 18,
                        "sum_other_doc_count": 3887,
                        "buckets": [
                            {"key": "/help/question", "doc_count": 807},
                            {"key": "/help/problem", "doc_count": 90},
                            {"key": "/public/news.php", "doc_count": 60},
                            {"key": "/adviser/index", "doc_count": 36},
                            {"key": "/Api/qyWap", "doc_count": 34},
                            {"key": "/consult/2-47-313724.html", "doc_count": 11},
                            {"key": "/qy/gszc", "doc_count": 11},
                            {"key": "/consult/2-47-298286.html", "doc_count": 10},
                            {"key": "/ad/2009042501.jpg", "doc_count": 9},
                            {"key": "/consult/2-47-307441.html", "doc_count": 9},
                            {"key": "/qy/djztc.html", "doc_count": 9},
                            {"key": "/qy/gsbgfw.html", "doc_count": 9},
                            {"key": "/user/suggest.html", "doc_count": 9},
                            {"key": "/ad/2008100302.jpg", "doc_count": 8},
                            {"key": "/ad/2008100401.jpg", "doc_count": 8},
                            {"key": "/consult/2-50-21716.html", "doc_count": 8},
                            {"key": "/ad/2008100402.jpg", "doc_count": 7},
                            {"key": "/consult/2-19-19912.html", "doc_count": 7},
                            {"key": "/consult/2-47-12758.html", "doc_count": 7},
                            {"key": "/consult/2-47-16648.html", "doc_count": 7},
                        ],
                    },
                },
                {
                    "key": "499",
                    "doc_count": 1630,
                    "path": {
                        "doc_count_error_upper_bound": 16,
                        "sum_other_doc_count": 656,
                        "buckets": [
                            {"key": "/ajax/get_ajax_main_kefu_html", "doc_count": 199},
                            {"key": "/help/question", "doc_count": 113},
                            {"key": "/Api/QyWapV2", "doc_count": 74},
                            {"key": "/ajax/get_ajax_main_public_html", "doc_count": 73},
                            {"key": "/consult/2-49-202097.html", "doc_count": 35},
                            {"key": "/ajax/show_static", "doc_count": 34},
                            {"key": "/consult/2-49-330466.html", "doc_count": 31},
                            {"key": "/consult/2-49-311723.html", "doc_count": 29},
                            {"key": "/consult/3-51052.html", "doc_count": 29},
                            {"key": "/consult/2-51-11786.html", "doc_count": 28},
                            {"key": "/consult/2-49-40986.html", "doc_count": 27},
                            {"key": "/consult/2-47-11640.html", "doc_count": 26},
                            {"key": "/consult/2-50-272829.html", "doc_count": 26},
                            {"key": "/consult/2-50-317193.html", "doc_count": 25},
                            {"key": "/consult/2-74-271584.html", "doc_count": 25},
                            {"key": "/consult/2-47-275421.html", "doc_count": 24},
                            {"key": "/consult/2-47-301799.html", "doc_count": 24},
                            {"key": "/consult/2-50-301233.html", "doc_count": 23},
                            {"key": "/consult/2-47-361899.html", "doc_count": 22},
                            {"key": "/consult/2-50-319126.html", "doc_count": 22},
                        ],
                    },
                },
                {
                    "key": "304",
                    "doc_count": 143,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "/public/js", "doc_count": 33},
                            {"key": "/themes/simplebootx", "doc_count": 17},
                            {"key": "/public/ym", "doc_count": 11},
                        ],
                    },
                },
                {
                    "key": "403",
                    "doc_count": 128,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {
                                "key": "/ajax/get_ajax_main_public_html",
                                "doc_count": 122,
                            },
                            {"key": "/ajax/show_static", "doc_count": 1},
                        ],
                    },
                },
                {
                    "key": "206",
                    "doc_count": 2,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "/public/error404", "doc_count": 2}],
                    },
                },
            ],
        },
        "city": {
            "doc_count_error_upper_bound": 596,
            "sum_other_doc_count": 44011,
            "buckets": [
                {
                    "key": "Beijing",
                    "doc_count": 873849,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 873849, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "uBSZ_IwB043sXHpDKaAu",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Zhengzhou",
                    "doc_count": 744491,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 744491, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "B0lQBY0BZnyrIs2wTB5_",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shanghai",
                    "doc_count": 74826,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 74826, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "m3ePFY0BZnyrIs2wI1-w",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shanghai",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Boydton",
                    "doc_count": 67220,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 67220, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "oqH4-owBZnyrIs2wBeUC",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Chengdu",
                    "doc_count": 45367,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 45367, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "wW8FEY0B043sXHpDt6K5",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Sichuan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shenzhen",
                    "doc_count": 37530,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 37530, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "SEZHBY0BZnyrIs2wcsoB",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Hangzhou",
                    "doc_count": 27596,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 27596, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "Bf9bC40B043sXHpDYUbW",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "New York",
                    "doc_count": 19620,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 19620, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "bHiQFY0BZnyrIs2wFpq_",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "New York",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Guangzhou",
                    "doc_count": 10945,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 10945, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "jEC6D40B043sXHpDgq71",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Qingdao",
                    "doc_count": 5494,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 5494, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "9IqqC40B043sXHpDSRXX",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shandong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Luoyang",
                    "doc_count": 5469,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 5469, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "v07yGY0BZnyrIs2w1wza",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Xi'an",
                    "doc_count": 3127,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3127, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "zQgyAI0B043sXHpDN2Dm",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Wuhan",
                    "doc_count": 2957,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2957, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "IuYGFo0BZnyrIs2w6DcO",
                                    "_score": 2.0,
                                    "_ignored": ["UA.keyword"],
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Hubei",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Nanjing",
                    "doc_count": 2525,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2525, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "9QEjAI0B043sXHpD1yJU",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Jiangsu",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Changsha",
                    "doc_count": 2302,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2302, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "OC1lAI0B043sXHpDVqGt",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Hunan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Chongqing",
                    "doc_count": 1908,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1908, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "5BQ0AI0BZnyrIs2wDx_5",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Chongqing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Jinan",
                    "doc_count": 1738,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1738, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "JTlzAI0B043sXHpD8hrl",
                                    "_score": 2.0,
                                    "_ignored": ["UA.keyword"],
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shandong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Fuzhou",
                    "doc_count": 1700,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1700, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "jq4Z-4wBZnyrIs2w1n2k",
                                    "_score": 2.0,
                                    "_ignored": ["UA.keyword"],
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Fujian",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Singapore",
                    "doc_count": 1657,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1657, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "tUjzGY0B043sXHpDZ1e3",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "Singapore"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Foshan",
                    "doc_count": 1653,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1653, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "2rc4C40BZnyrIs2w1Rxf",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "clientip": {
            "doc_count_error_upper_bound": 7545,
            "sum_other_doc_count": 2497268,
            "buckets": [
                {
                    "key": "154.38.79.1",
                    "doc_count": 2685429,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2685429, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "z0bvGY0B043sXHpDq8XP",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {"country_name": "United States"}
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.243.240",
                    "doc_count": 38029,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 38029, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "d0fiGY0BZnyrIs2wCqB5",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "123.160.242.166",
                    "doc_count": 35688,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 35688, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "kw5gC40B043sXHpD0Wc3",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.0.18",
                    "doc_count": 35349,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 35349, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "BYytC40B043sXHpDX8sV",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.241.173",
                    "doc_count": 31114,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 31114, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "vzObD40B043sXHpDYZut",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "171.8.173.234",
                    "doc_count": 30014,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 30014, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "iGIoCY0B043sXHpD2qrg",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "106.42.109.239",
                    "doc_count": 25203,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 25203, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "av8fAI0B043sXHpD2iJr",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "47.107.254.32",
                    "doc_count": 23975,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 23975, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "FkVEBY0BZnyrIs2w5PF5",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "121.41.74.221",
                    "doc_count": 21273,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 21273, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "gcdZAY0B043sXHpDPLqP",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "47.76.35.19",
                    "doc_count": 19484,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 19484, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "SaP7-owBZnyrIs2w-zkg",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "New York",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "115.223.43.220",
                    "doc_count": 15203,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 15203, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "IObdEo0BZnyrIs2wlFOn",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "111.12.229.54",
                    "doc_count": 14054,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 14054, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "dYLLF40B043sXHpDjzzg",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "171.8.172.245",
                    "doc_count": 13600,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 13600, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "xklQBY0BZnyrIs2w40rF",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "183.220.120.15",
                    "doc_count": 11841,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 11841, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "U7bkFY0B043sXHpDV56s",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Sichuan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.243.241",
                    "doc_count": 11460,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 11460, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "WM5xA40BZnyrIs2wacDf",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "171.8.172.214",
                    "doc_count": 11408,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 11408, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "620tCY0BZnyrIs2w9xha",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.243.209",
                    "doc_count": 10719,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 10719, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "gm0tCY0BZnyrIs2w2BQO",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "183.220.120.8",
                    "doc_count": 8929,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 8929, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "YCad_IwBZnyrIs2wvUTc",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Sichuan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.242.178",
                    "doc_count": 8755,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 8755, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "X0lSBY0BZnyrIs2wosYN",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.241.183",
                    "doc_count": 8025,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 8025, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "bKYwC40BZnyrIs2waDwc",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "day": {
            "buckets": [
                {
                    "key_as_string": "2024-01-12",
                    "key": 1705017600000,
                    "doc_count": 843276,
                },
                {
                    "key_as_string": "2024-01-13",
                    "key": 1705104000000,
                    "doc_count": 923383,
                },
                {
                    "key_as_string": "2024-01-14",
                    "key": 1705190400000,
                    "doc_count": 1191364,
                },
                {
                    "key_as_string": "2024-01-15",
                    "key": 1705276800000,
                    "doc_count": 894610,
                },
                {
                    "key_as_string": "2024-01-16",
                    "key": 1705363200000,
                    "doc_count": 825496,
                },
                {
                    "key_as_string": "2024-01-17",
                    "key": 1705449600000,
                    "doc_count": 772516,
                },
                {
                    "key_as_string": "2024-01-18",
                    "key": 1705536000000,
                    "doc_count": 106175,
                },
            ]
        },
    },
    {
        "key": "wd.xxxx.com",
        "doc_count": 2724075,
        "path": {
            "doc_count_error_upper_bound": 97,
            "sum_other_doc_count": 2479054,
            "buckets": [
                {
                    "key": "/ajax/create_price",
                    "doc_count": 158207,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 157630},
                            {"key": "499", "doc_count": 577},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07999999821186066,
                            "95.0": 0.08299999684095383,
                            "99.0": 0.09478411453202203,
                        }
                    },
                },
                {
                    "key": "/ajax/show_static",
                    "doc_count": 24844,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 24807},
                            {"key": "499", "doc_count": 37},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07500000298023224,
                            "95.0": 0.09088333288473731,
                            "99.0": 1.61907675436565,
                        }
                    },
                },
                {
                    "key": "/HtmlAjax/getGoodsSearchHtml",
                    "doc_count": 19747,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 19737},
                            {"key": "499", "doc_count": 10},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.080277549794742,
                            "95.0": 0.2032606404857703,
                            "99.0": 1.620515011293547,
                        }
                    },
                },
                {
                    "key": "/spread/syncImage",
                    "doc_count": 4408,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 4408}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.12099999934434891,
                            "95.0": 0.12399999797344208,
                            "99.0": 0.13099999725818634,
                        }
                    },
                },
                {
                    "key": "/public/error404",
                    "doc_count": 4185,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 4144},
                            {"key": "304", "doc_count": 39},
                            {"key": "206", "doc_count": 2},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.571520843356848,
                            "95.0": 1.815041720867157,
                            "99.0": 2.2958500027656523,
                        }
                    },
                },
                {
                    "key": "/ajax/amhSearch",
                    "doc_count": 3916,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 2760},
                            {"key": "499", "doc_count": 1156},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07000000029802322,
                            "95.0": 0.07319999933242793,
                            "99.0": 0.07999999821186066,
                        }
                    },
                },
                {
                    "key": "/HtmlAjax/getGoodsDetailHtml",
                    "doc_count": 3267,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 3257},
                            {"key": "499", "doc_count": 10},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07100000232458115,
                            "95.0": 0.0750375027768313,
                            "99.0": 1.3828300082683562,
                        }
                    },
                },
                {
                    "key": "/BuryingPoint/record",
                    "doc_count": 1090,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 602},
                            {"key": "499", "doc_count": 488},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.06675000116229057,
                            "95.0": 0.0689999982714653,
                            "99.0": 0.07500000298023224,
                        }
                    },
                },
                {
                    "key": "/ajax/amhSearch_checkbox",
                    "doc_count": 886,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 603},
                            {"key": "499", "doc_count": 283},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.0689999982714653,
                            "95.0": 0.0729999989271164,
                            "99.0": 0.07800000160932541,
                        }
                    },
                },
                {
                    "key": "/ajax/addPeople",
                    "doc_count": 561,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 556},
                            {"key": "499", "doc_count": 5},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.09439999759197237,
                            "95.0": 1.349700021743774,
                            "99.0": 1.9082000136375388,
                        }
                    },
                },
                {
                    "key": "/taobao/s-----------------5.html",
                    "doc_count": 561,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 561}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.34879999160766606,
                            "95.0": 0.36989998966455445,
                            "99.0": 0.7319999933242798,
                        }
                    },
                },
                {
                    "key": "/taobao/s--2-----------------1.html",
                    "doc_count": 218,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 218}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.3569999933242798,
                            "95.0": 0.37900000214576723,
                            "99.0": 1.69651997566223,
                        }
                    },
                },
                {
                    "key": "/other/s---33------------1.html",
                    "doc_count": 217,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 217}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.16980000138282778,
                            "95.0": 0.17594999894499772,
                            "99.0": 0.19697000190615638,
                        }
                    },
                },
                {
                    "key": "/other/s---26------------1.html",
                    "doc_count": 208,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 206},
                            {"key": "499", "doc_count": 2},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.16099999845027924,
                            "95.0": 0.18189999461174006,
                            "99.0": 4.973859794139764,
                        }
                    },
                },
                {
                    "key": "/other/s---28------------1.html",
                    "doc_count": 191,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 191}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.1720000058412552,
                            "95.0": 0.17690000087022778,
                            "99.0": 0.1977200044691563,
                        }
                    },
                },
                {
                    "key": "/other/s---34------------1.html",
                    "doc_count": 179,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 179}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.17299999296665192,
                            "95.0": 0.18154999539256095,
                            "99.0": 0.28137999191880286,
                        }
                    },
                },
                {
                    "key": "/taobao/s--4---------------1.html",
                    "doc_count": 150,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 147},
                            {"key": "499", "doc_count": 3},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.3724999874830246,
                            "95.0": 0.4860000014305115,
                            "99.0": 9.494000434875488,
                        }
                    },
                },
                {
                    "key": "/other/s---5------------1.html",
                    "doc_count": 143,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 142},
                            {"key": "499", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.17539999783039095,
                            "95.0": 0.18374999985098836,
                            "99.0": 1.2664900118111944,
                        }
                    },
                },
                {
                    "key": "/taobao/s--8-----------------1.html",
                    "doc_count": 135,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 132},
                            {"key": "499", "doc_count": 3},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.34599998593330383,
                            "95.0": 0.36400000751018524,
                            "99.0": 9.704150009155274,
                        }
                    },
                },
                {
                    "key": "/public/js",
                    "doc_count": 68,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 68}],
                    },
                    "time": {"values": {"90.0": 0.0, "95.0": 0.0, "99.0": 0.0}},
                },
            ],
        },
        "code": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "200",
                    "doc_count": 2713494,
                    "path": {
                        "doc_count_error_upper_bound": 93,
                        "sum_other_doc_count": 2471692,
                        "buckets": [
                            {"key": "/ajax/create_price", "doc_count": 157630},
                            {"key": "/ajax/show_static", "doc_count": 24807},
                            {"key": "/HtmlAjax/getGoodsSearchHtml", "doc_count": 19737},
                            {"key": "/spread/syncImage", "doc_count": 4408},
                            {"key": "/public/error404", "doc_count": 4144},
                            {"key": "/HtmlAjax/getGoodsDetailHtml", "doc_count": 3257},
                            {"key": "/ajax/amhSearch", "doc_count": 2760},
                            {"key": "/ajax/amhSearch_checkbox", "doc_count": 605},
                            {"key": "/BuryingPoint/record", "doc_count": 602},
                            {
                                "key": "/taobao/s-----------------5.html",
                                "doc_count": 561,
                            },
                            {"key": "/ajax/addPeople", "doc_count": 556},
                            {
                                "key": "/taobao/s--2-----------------1.html",
                                "doc_count": 220,
                            },
                            {
                                "key": "/other/s---33------------1.html",
                                "doc_count": 217,
                            },
                            {
                                "key": "/other/s---26------------1.html",
                                "doc_count": 206,
                            },
                            {
                                "key": "/other/s---28------------1.html",
                                "doc_count": 191,
                            },
                            {
                                "key": "/other/s---34------------1.html",
                                "doc_count": 179,
                            },
                            {
                                "key": "/taobao/s--4---------------1.html",
                                "doc_count": 147,
                            },
                            {"key": "/other/s---5------------1.html", "doc_count": 146},
                            {
                                "key": "/taobao/s--8-----------------1.html",
                                "doc_count": 137,
                            },
                            {"key": "/public/js", "doc_count": 68},
                        ],
                    },
                },
                {
                    "key": "403",
                    "doc_count": 5841,
                    "path": {
                        "doc_count_error_upper_bound": 18,
                        "sum_other_doc_count": 5746,
                        "buckets": [
                            {"key": "/jd/752539.html", "doc_count": 4},
                            {
                                "key": "/taobao/s--3-11----------------1.html",
                                "doc_count": 4,
                            },
                            {"key": "/jd/651442288269983745.html", "doc_count": 3},
                            {"key": "/jd/651803791770779651.html", "doc_count": 3},
                            {"key": "/jd/651839553635614721.html", "doc_count": 3},
                            {"key": "/jd/667681730177531905.html", "doc_count": 3},
                            {"key": "/jd/711243.html", "doc_count": 3},
                            {"key": "/jd/1066084.html", "doc_count": 2},
                            {"key": "/jd/625728151825154049.html", "doc_count": 2},
                            {"key": "/jd/650327325321199619.html", "doc_count": 2},
                            {"key": "/jd/650377937459085314.html", "doc_count": 2},
                            {"key": "/jd/650623339420712961.html", "doc_count": 2},
                            {"key": "/jd/650634833021632516.html", "doc_count": 2},
                            {"key": "/jd/650658049106640898.html", "doc_count": 2},
                            {"key": "/jd/650727788919128065.html", "doc_count": 2},
                            {"key": "/jd/650992889425297409.html", "doc_count": 2},
                            {"key": "/jd/651061357134741505.html", "doc_count": 2},
                            {"key": "/jd/651092662820012033.html", "doc_count": 2},
                            {"key": "/jd/651376183174234113.html", "doc_count": 2},
                            {"key": "/jd/651810092940787713.html", "doc_count": 2},
                        ],
                    },
                },
                {
                    "key": "499",
                    "doc_count": 3557,
                    "path": {
                        "doc_count_error_upper_bound": 6,
                        "sum_other_doc_count": 866,
                        "buckets": [
                            {"key": "/ajax/amhSearch", "doc_count": 1156},
                            {"key": "/ajax/create_price", "doc_count": 577},
                            {"key": "/BuryingPoint/record", "doc_count": 488},
                            {"key": "/ajax/amhSearch_checkbox", "doc_count": 283},
                            {"key": "/ajax/show_static", "doc_count": 36},
                            {"key": "/consulte/2-200-371945.html", "doc_count": 14},
                            {"key": "/HtmlAjax/getGoodsDetailHtml", "doc_count": 10},
                            {"key": "/HtmlAjax/getGoodsSearchHtml", "doc_count": 9},
                            {"key": "/jd/s--1--------------1.html", "doc_count": 5},
                            {"key": "/ajax/addPeople", "doc_count": 4},
                            {"key": "/jd/s--12--------------1.html", "doc_count": 4},
                            {"key": "/jd/s--14--------------1.html", "doc_count": 4},
                            {"key": "/jd/s--23--------------1.html", "doc_count": 4},
                            {"key": "/mgj/s--3-------------1.html", "doc_count": 4},
                            {"key": "/other/s--11------------1.html", "doc_count": 4},
                            {"key": "/other/s--9------------1.html", "doc_count": 4},
                            {
                                "key": "/taobao/s--14---------------1.html",
                                "doc_count": 4,
                            },
                            {
                                "key": "/taobao/s--5---------------1.html",
                                "doc_count": 4,
                            },
                            {
                                "key": "/taobao/s--7---------------1.html",
                                "doc_count": 4,
                            },
                            {
                                "key": "/tmall-gold/s--14----------------1.html",
                                "doc_count": 4,
                            },
                        ],
                    },
                },
                {
                    "key": "404",
                    "doc_count": 902,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 132,
                        "buckets": [
                            {"key": "/help/problem", "doc_count": 60},
                            {"key": "/user/ticketSystem", "doc_count": 24},
                            {"key": "/css/modules", "doc_count": 18},
                            {"key": "/taobao.html/trackback", "doc_count": 18},
                            {"key": "/products/list", "doc_count": 16},
                            {"key": "/wjxx/2024", "doc_count": 15},
                            {"key": "/help/index", "doc_count": 13},
                            {"key": "/api/cart", "doc_count": 12},
                            {"key": "/consult/3-105.html", "doc_count": 12},
                            {"key": "/e/DoInfo", "doc_count": 12},
                            {"key": "/include/ckeditor", "doc_count": 12},
                            {"key": "/user/login", "doc_count": 12},
                            {"key": "/user/register.html", "doc_count": 12},
                            {"key": "/cjpd/2024", "doc_count": 11},
                            {"key": "/plus/ad_js.php", "doc_count": 10},
                            {"key": "/plus/flink_add.php", "doc_count": 10},
                            {"key": "/jryw/2024", "doc_count": 8},
                            {"key": "/consult/2-47-313026.html", "doc_count": 6},
                            {"key": "/consult/3-12.html", "doc_count": 6},
                            {"key": "/consult/3-18474.html", "doc_count": 6},
                        ],
                    },
                },
                {
                    "key": "302",
                    "doc_count": 218,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 128,
                        "buckets": [
                            {"key": "/answer/1-53675-", "doc_count": 9},
                            {"key": "/answer/1-54103-", "doc_count": 8},
                            {"key": "/answer/1-54317-", "doc_count": 6},
                            {"key": "/answer/1-304184-", "doc_count": 5},
                            {"key": "/answer/1-200603-", "doc_count": 4},
                            {"key": "/answer/1-201245-", "doc_count": 4},
                            {"key": "/answer/1-303838-", "doc_count": 4},
                            {"key": "/answer/1-303895-", "doc_count": 4},
                            {"key": "/answer/1-303917-", "doc_count": 4},
                            {"key": "/answer/1-303978-", "doc_count": 4},
                            {"key": "/answer/1-304088-", "doc_count": 4},
                            {"key": "/answer/1-304144-", "doc_count": 4},
                            {"key": "/answer/1-54917-", "doc_count": 4},
                            {"key": "/answer/1-303905-", "doc_count": 3},
                            {"key": "/answer/1-303981-", "doc_count": 3},
                            {"key": "/answer/1-53745-", "doc_count": 3},
                            {"key": "/answer/1-54230-", "doc_count": 3},
                            {"key": "/answer/1-54456-", "doc_count": 3},
                            {"key": "/answer/1-2843-", "doc_count": 2},
                            {"key": "/answer/1-303562-", "doc_count": 2},
                        ],
                    },
                },
                {
                    "key": "304",
                    "doc_count": 55,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "/public/error404", "doc_count": 39}],
                    },
                },
                {
                    "key": "502",
                    "doc_count": 5,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "/mgj/s--14-1------------1.html", "doc_count": 1},
                            {
                                "key": "/taobao/s--3---------------1.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/tmall-gold/s--2----------------1.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/tmall/s---7---------------1.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/tmall/s--3----------------1.html",
                                "doc_count": 1,
                            },
                        ],
                    },
                },
                {
                    "key": "206",
                    "doc_count": 2,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "/public/error404", "doc_count": 2}],
                    },
                },
                {
                    "key": "301",
                    "doc_count": 1,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [],
                    },
                },
            ],
        },
        "city": {
            "doc_count_error_upper_bound": 134,
            "sum_other_doc_count": 15618,
            "buckets": [
                {
                    "key": "Beijing",
                    "doc_count": 748006,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 748006, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "qDxFBY0B043sXHpD0NRs",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Zhengzhou",
                    "doc_count": 709611,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 709611, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "4XYEEY0BZnyrIs2w-6BH",
                                    "_score": 2.0,
                                    "_ignored": ["UA.keyword"],
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Hangzhou",
                    "doc_count": 199739,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 199739, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "QUDeGY0B043sXHpDzXIf",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Ashburn",
                    "doc_count": 22094,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 22094, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "SJG6FI0B043sXHpDVQJC",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Boydton",
                    "doc_count": 20096,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 20096, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "BEbvGY0B043sXHpD4tNh",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shenzhen",
                    "doc_count": 10476,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 10476, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "mcVTAY0B043sXHpDxVWc",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Luoyang",
                    "doc_count": 9236,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 9236, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "kSp5C40B043sXHpDZcjf",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Guangzhou",
                    "doc_count": 5475,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 5475, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "xChgAI0B043sXHpDYQhA",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shanghai",
                    "doc_count": 5304,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 5304, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "noGgFY0B043sXHpDU19g",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shanghai",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Chengdu",
                    "doc_count": 5073,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 5073, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "uHP4BY0B043sXHpDqXgd",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Sichuan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Jinhua",
                    "doc_count": 1502,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1502, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "p11gFo0B043sXHpDzsbR",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Xi'an",
                    "doc_count": 1345,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1345, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "tg_QB40BZnyrIs2wx9XK",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Nanjing",
                    "doc_count": 1045,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1045, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "eY__D40BZnyrIs2wrmyn",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Jiangsu",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shijiazhuang",
                    "doc_count": 1013,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1013, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "SBFFAI0B043sXHpDvsJ1",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Hebei",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Wuhan",
                    "doc_count": 935,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 935, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "upFhBo0B043sXHpDWD7k",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Hubei",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Xiamen",
                    "doc_count": 799,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 799, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "IgEYFo0BZnyrIs2w_RgG",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Fujian",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Dongguan",
                    "doc_count": 725,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 725, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "h8c2EI0B043sXHpD0Zjr",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Quanzhou",
                    "doc_count": 665,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 665, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "LG8FEY0B043sXHpDc2tA",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Fujian",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Wuxi",
                    "doc_count": 616,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 616, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "1eJm_IwB043sXHpDRGLV",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Jiangsu",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Lu'an",
                    "doc_count": 590,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 590, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "vcZ1A40B043sXHpDwHIZ",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Anhui",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "clientip": {
            "doc_count_error_upper_bound": 6031,
            "sum_other_doc_count": 1940805,
            "buckets": [
                {
                    "key": "121.41.74.221",
                    "doc_count": 141219,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 141219, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "e9VxAY0B043sXHpDlNiN",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.49",
                    "doc_count": 88934,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 88934, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "HCHDBI0BZnyrIs2wDaaM",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.62",
                    "doc_count": 87229,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 87229, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "kDcxDI0BZnyrIs2wscpK",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.76",
                    "doc_count": 76953,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 76953, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "DW8EEY0B043sXHpD_gWo",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.43",
                    "doc_count": 68376,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 68376, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "R3ePFY0BZnyrIs2wH1z_",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.243.240",
                    "doc_count": 43300,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 43300, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "6q02C40B043sXHpDRa6I",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.241.173",
                    "doc_count": 35257,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 35257, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "gXCPFY0B043sXHpDHwT4",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.60",
                    "doc_count": 34236,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 34236, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "IKYwC40BZnyrIs2wZCxS",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "171.8.173.234",
                    "doc_count": 26841,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 26841, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "R2QvCY0B043sXHpDFGya",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "123.160.242.166",
                    "doc_count": 26497,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 26497, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "8KtrCo0B043sXHpDtGTX",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.0.18",
                    "doc_count": 26339,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 26339, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "bjeSD40BZnyrIs2wFAIU",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "106.42.109.239",
                    "doc_count": 23625,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 23625, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "LXiPFY0BZnyrIs2w51PW",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "171.8.172.245",
                    "doc_count": 17068,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 17068, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "sz5KBY0B043sXHpDWw98",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "171.15.11.228",
                    "doc_count": 16125,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 16125, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "tUj0GY0B043sXHpDQp-q",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "123.52.20.86",
                    "doc_count": 15878,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 15878, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "nkLkGY0B043sXHpDe3MK",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "171.8.172.214",
                    "doc_count": 13917,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 13917, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "uG0vCY0BZnyrIs2wEFW9",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.243.209",
                    "doc_count": 11051,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 11051, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "VlrfCI0BZnyrIs2wm8jH",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.243.241",
                    "doc_count": 10898,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 10898, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "wuTGA40BZnyrIs2w0gS9",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "120.245.60.157",
                    "doc_count": 10278,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 10278, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "0I-4FI0B043sXHpDf-T3",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.192.242.181",
                    "doc_count": 9249,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 9249, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "Pxd9E40B043sXHpDm6xd",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "day": {
            "buckets": [
                {
                    "key_as_string": "2024-01-12",
                    "key": 1705017600000,
                    "doc_count": 83356,
                },
                {
                    "key_as_string": "2024-01-13",
                    "key": 1705104000000,
                    "doc_count": 247323,
                },
                {
                    "key_as_string": "2024-01-14",
                    "key": 1705190400000,
                    "doc_count": 624759,
                },
                {
                    "key_as_string": "2024-01-15",
                    "key": 1705276800000,
                    "doc_count": 678221,
                },
                {
                    "key_as_string": "2024-01-16",
                    "key": 1705363200000,
                    "doc_count": 511467,
                },
                {
                    "key_as_string": "2024-01-17",
                    "key": 1705449600000,
                    "doc_count": 546746,
                },
                {
                    "key_as_string": "2024-01-18",
                    "key": 1705536000000,
                    "doc_count": 32203,
                },
            ]
        },
    },
    {
        "key": "r.yuzhua.com",
        "doc_count": 1983577,
        "path": {
            "doc_count_error_upper_bound": 193,
            "sum_other_doc_count": 1467835,
            "buckets": [
                {
                    "key": "/index.php/Ajax",
                    "doc_count": 92073,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 92062},
                            {"key": "499", "doc_count": 10},
                            {"key": "301", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.017999999225139618,
                            "95.0": 0.017999999225139618,
                            "99.0": 0.02199999988079071,
                        }
                    },
                },
                {
                    "key": "/ajax/show_static",
                    "doc_count": 87229,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 87220},
                            {"key": "499", "doc_count": 9},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.01600000075995922,
                            "95.0": 0.017000000923871994,
                            "99.0": 0.020999999716877937,
                        }
                    },
                },
                {
                    "key": "/BuryingPoint/browseSync",
                    "doc_count": 53411,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 52871},
                            {"key": "499", "doc_count": 539},
                            {"key": "301", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.006000000052154064,
                            "95.0": 0.006000000052154064,
                            "99.0": 0.008999999612569809,
                        }
                    },
                },
                {
                    "key": "/HtmlAjax/list_recommend_list_html",
                    "doc_count": 48152,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 48130},
                            {"key": "499", "doc_count": 21},
                            {"key": "301", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.026000000536441803,
                            "95.0": 0.02800000086426735,
                            "99.0": 0.11483323995634466,
                        }
                    },
                },
                {
                    "key": "/static/api",
                    "doc_count": 13996,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 13986},
                            {"key": "304", "doc_count": 10},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.003000000026077032,
                            "95.0": 0.003000000026077032,
                            "99.0": 0.004000000189989805,
                        }
                    },
                },
                {
                    "key": "/BuryingPoint/clickSync",
                    "doc_count": 12901,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 12884},
                            {"key": "499", "doc_count": 17},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.005975555603702855,
                            "95.0": 0.006000000052154064,
                            "99.0": 0.00800000037997961,
                        }
                    },
                },
                {
                    "key": "/public/js",
                    "doc_count": 9415,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 9412},
                            {"key": "304", "doc_count": 3},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.0,
                            "95.0": 0.0010000000474974513,
                            "99.0": 0.0010000000474974513,
                        }
                    },
                },
                {
                    "key": "/HtmlAjax/detail_similarity_data_html",
                    "doc_count": 8730,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 8713},
                            {"key": "499", "doc_count": 15},
                            {"key": "301", "doc_count": 1},
                            {"key": "404", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.035999998450279236,
                            "95.0": 0.03799999877810478,
                            "99.0": 0.2909999926885006,
                        }
                    },
                },
                {
                    "key": "/HtmlAjax/detail_problems_html",
                    "doc_count": 8716,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 8714},
                            {"key": "301", "doc_count": 1},
                            {"key": "499", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.027000000700354576,
                            "95.0": 0.02800000086426735,
                            "99.0": 0.1749199968576432,
                        }
                    },
                },
                {
                    "key": "/ajax/add_type_search_keyword",
                    "doc_count": 7116,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 7115},
                            {"key": "499", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.01899999938905239,
                            "95.0": 0.019999999552965164,
                            "99.0": 0.023000000044703484,
                        }
                    },
                },
                {
                    "key": "/ApiToYzApp/getBrandIndexSearchParams",
                    "doc_count": 6832,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 6832}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.008999999612569809,
                            "95.0": 0.009999999776482582,
                            "99.0": 0.013000000268220901,
                        }
                    },
                },
                {
                    "key": "/HtmlAjax/index_post_html",
                    "doc_count": 5505,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 5502},
                            {"key": "499", "doc_count": 2},
                            {"key": "301", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.03799999877810478,
                            "95.0": 0.6519000113010406,
                            "99.0": 0.7907125122845171,
                        }
                    },
                },
                {
                    "key": "/ajax/addPeople",
                    "doc_count": 5505,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 5503},
                            {"key": "499", "doc_count": 2},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.017500000074505806,
                            "95.0": 0.30000001192092896,
                            "99.0": 0.32499998807907104,
                        }
                    },
                },
                {
                    "key": "/index.php/NewIndex",
                    "doc_count": 5505,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 5505}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.028999999165534973,
                            "95.0": 0.0373106055770709,
                            "99.0": 0.2240000069141388,
                        }
                    },
                },
                {
                    "key": "/HtmlAjax/ipr_trade_bar_html",
                    "doc_count": 5504,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 5503},
                            {"key": "301", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.02500000037252903,
                            "95.0": 0.026000000536441803,
                            "99.0": 0.029999999329447746,
                        }
                    },
                },
                {
                    "key": "/ajax/get_global_count",
                    "doc_count": 3141,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 3111},
                            {"key": "499", "doc_count": 30},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.017999999225139618,
                            "95.0": 0.01899999938905239,
                            "99.0": 0.02199999988079071,
                        }
                    },
                },
                {
                    "key": "/ajax/get_mark_sum_deal",
                    "doc_count": 2513,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 2513}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.019999999552965164,
                            "95.0": 0.020999999716877937,
                            "99.0": 0.024000000208616257,
                        }
                    },
                },
                {
                    "key": "/consulte/result",
                    "doc_count": 1153,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 1145},
                            {"key": "499", "doc_count": 8},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.8639999628067017,
                            "95.0": 3.0480000972747803,
                            "99.0": 3.260729923248291,
                        }
                    },
                },
                {
                    "key": "/search/css",
                    "doc_count": 793,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 793}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.5381333192189535,
                            "95.0": 0.5878500014543533,
                            "99.0": 0.7032799798250196,
                        }
                    },
                },
                {
                    "key": "/ajax/all_term_show",
                    "doc_count": 749,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 749}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.1469999998807907,
                            "95.0": 0.15700000524520874,
                            "99.0": 0.18901999562978744,
                        }
                    },
                },
            ],
        },
        "code": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "200",
                    "doc_count": 1837285,
                    "path": {
                        "doc_count_error_upper_bound": 183,
                        "sum_other_doc_count": 1326504,
                        "buckets": [
                            {"key": "/index.php/Ajax", "doc_count": 92062},
                            {"key": "/ajax/show_static", "doc_count": 87220},
                            {"key": "/BuryingPoint/browseSync", "doc_count": 52871},
                            {
                                "key": "/HtmlAjax/list_recommend_list_html",
                                "doc_count": 48130,
                            },
                            {"key": "/static/api", "doc_count": 13986},
                            {"key": "/BuryingPoint/clickSync", "doc_count": 12884},
                            {"key": "/public/js", "doc_count": 9412},
                            {
                                "key": "/HtmlAjax/detail_problems_html",
                                "doc_count": 8714,
                            },
                            {
                                "key": "/HtmlAjax/detail_similarity_data_html",
                                "doc_count": 8713,
                            },
                            {"key": "/ajax/add_type_search_keyword", "doc_count": 7115},
                            {
                                "key": "/ApiToYzApp/getBrandIndexSearchParams",
                                "doc_count": 6832,
                            },
                            {"key": "/index.php/NewIndex", "doc_count": 5505},
                            {"key": "/HtmlAjax/ipr_trade_bar_html", "doc_count": 5503},
                            {"key": "/ajax/addPeople", "doc_count": 5503},
                            {"key": "/HtmlAjax/index_post_html", "doc_count": 5502},
                            {"key": "/ajax/get_global_count", "doc_count": 3111},
                            {"key": "/ajax/get_mark_sum_deal", "doc_count": 2513},
                            {"key": "/consulte/result", "doc_count": 1145},
                            {"key": "/search/css", "doc_count": 801},
                            {"key": "/ajax/all_term_show", "doc_count": 749},
                        ],
                    },
                },
                {
                    "key": "302",
                    "doc_count": 132849,
                    "path": {
                        "doc_count_error_upper_bound": 24,
                        "sum_other_doc_count": 132535,
                        "buckets": [
                            {"key": "/consulte/2-239-237.html", "doc_count": 68},
                            {"key": "/cgoods/2GK0712YBQ0M.html", "doc_count": 14},
                            {"key": "/cgoods/62B741EGR32M.html", "doc_count": 14},
                            {"key": "/cgoods/9Z36DJ7X9WWM.html", "doc_count": 14},
                            {"key": "/cgoods/KP5A6BK6DE0M.html", "doc_count": 14},
                            {"key": "/cgoods/UE0L9KRSTUHT.html", "doc_count": 13},
                            {"key": "/cgoods/UKM8TLUTSDZM.html", "doc_count": 12},
                            {"key": "/cgoods/CGW34WG8KTWM.html", "doc_count": 10},
                            {"key": "/cgoods/CUFDTWQX8KBM.html", "doc_count": 10},
                            {"key": "/cgoods/166WJUE06JBT.html", "doc_count": 9},
                            {"key": "/cgoods/61YYYY.html", "doc_count": 9},
                            {"key": "/cgoods/A03JC6P2MB2C.html", "doc_count": 9},
                            {"key": "/cgoods/TD3B4G72HPZT.html", "doc_count": 9},
                            {"key": "/cgoods/3N19FX5B0YMM.html", "doc_count": 8},
                            {"key": "/cgoods/BGQWF6M4HT1M.html", "doc_count": 8},
                            {"key": "/cgoods/JM1N89UDAWWM.html", "doc_count": 8},
                            {"key": "/cgoods/74L4C7ZQKB1M.html", "doc_count": 7},
                            {"key": "/cgoods/LUT11UAEBF8M.html", "doc_count": 7},
                            {"key": "/cgoods/MTYRYW07TGLM.html", "doc_count": 7},
                            {"key": "/cgoods/6B116L5N6Q3T.html", "doc_count": 6},
                        ],
                    },
                },
                {
                    "key": "301",
                    "doc_count": 7202,
                    "path": {
                        "doc_count_error_upper_bound": 21,
                        "sum_other_doc_count": 3337,
                        "buckets": [
                            {"key": "/consulte/2-19-324059.html", "doc_count": 27},
                            {"key": "/r/_nuxt", "doc_count": 17},
                            {"key": "/consulte/2-22-329208.html", "doc_count": 10},
                            {"key": "/search/------------4--1-.html", "doc_count": 10},
                            {"key": "/consulte/2-22-329015.html", "doc_count": 9},
                            {
                                "key": "/search/43--------------1----.html",
                                "doc_count": 9,
                            },
                            {"key": "/search/-----15000-30000--1.html", "doc_count": 8},
                            {
                                "key": "/search/25----------%25E5%2585%2583%25E7%25B4%25A0----1----.html",
                                "doc_count": 8,
                            },
                            {"key": "/goods/94Y0D9X1ZD.html", "doc_count": 7},
                            {
                                "key": "/search/03-0306-------------1----.html",
                                "doc_count": 7,
                            },
                            {
                                "key": "/search/28-0901,2804-------------1----.html",
                                "doc_count": 7,
                            },
                            {"key": "/consulte/2-22-307636.html", "doc_count": 6},
                            {
                                "key": "/global-search/25--------------1-----.html",
                                "doc_count": 6,
                            },
                            {"key": "/goods/DT1GJY.html", "doc_count": 6},
                            {
                                "key": "/search/02-0205-------------1----.html",
                                "doc_count": 6,
                            },
                            {
                                "key": "/search/32-3202-------------1----.html",
                                "doc_count": 6,
                            },
                            {"key": "/spread/get_goods_mobile", "doc_count": 6},
                            {"key": "/consulte/2-22-315529.html", "doc_count": 5},
                            {"key": "/consulte/2-22-328349.html", "doc_count": 5},
                            {"key": "/goods/U60QJY.html", "doc_count": 5},
                        ],
                    },
                },
                {
                    "key": "499",
                    "doc_count": 4427,
                    "path": {
                        "doc_count_error_upper_bound": 13,
                        "sum_other_doc_count": 3425,
                        "buckets": [
                            {"key": "/BuryingPoint/browseSync", "doc_count": 539},
                            {"key": "/ipr/gjsbzc.html", "doc_count": 34},
                            {"key": "/ajax/get_global_count", "doc_count": 28},
                            {
                                "key": "/HtmlAjax/list_recommend_list_html",
                                "doc_count": 20,
                            },
                            {"key": "/BuryingPoint/clickSync", "doc_count": 16},
                            {
                                "key": "/HtmlAjax/detail_similarity_data_html",
                                "doc_count": 14,
                            },
                            {"key": "/index.php/Ajax", "doc_count": 9},
                            {"key": "/ajax/show_static", "doc_count": 8},
                            {"key": "/consulte/result", "doc_count": 7},
                            {"key": "/search/--------------1----.html", "doc_count": 7},
                            {"key": "/catindex/07.html", "doc_count": 5},
                            {"key": "/goods/9PSJEY.html", "doc_count": 4},
                            {
                                "key": "/search/----------%25E8%25B4%25A4%25E5%2590%259B%25E7%25AB%25B9----1-----.html",
                                "doc_count": 4,
                            },
                            {"key": "/goods/JY2F57MTWE.html", "doc_count": 3},
                            {"key": "/goods/S1KL2C.html", "doc_count": 3},
                            {
                                "key": "/search/----------%25E6%259D%259C%25E5%2585%25AB%25E4%25BB%2599---------.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/search/----------%25E7%2587%2595%25E7%25AA%259D.html",
                                "doc_count": 3,
                            },
                            {"key": "/search/----------------.html", "doc_count": 3},
                            {
                                "key": "/search/--------------1-----%25E4%25BF%259D%25E5%2581%25A5%25E5%2593%2581.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/search/--------------1-----.html",
                                "doc_count": 3,
                            },
                        ],
                    },
                },
                {
                    "key": "404",
                    "doc_count": 1323,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 47,
                        "buckets": [
                            {"key": "/user/register.html", "doc_count": 494},
                            {"key": "/css/modules", "doc_count": 123},
                            {"key": "/user/login.html", "doc_count": 120},
                            {"key": "/help/problem", "doc_count": 84},
                            {"key": "/help/question.html", "doc_count": 78},
                            {"key": "/data/upload", "doc_count": 75},
                            {"key": "/api/cart", "doc_count": 48},
                            {"key": "/include/ckeditor", "doc_count": 15},
                            {
                                "key": "/.well-known/apple-app-site-association",
                                "doc_count": 11,
                            },
                            {"key": "/plus/ad_js.php", "doc_count": 11},
                            {"key": "/plus/flink_add.php", "doc_count": 11},
                            {"key": "/e/DoInfo", "doc_count": 10},
                            {"key": "/consult/3-105.html", "doc_count": 6},
                            {"key": "/consult/3-12.html", "doc_count": 6},
                            {"key": "/help/index", "doc_count": 6},
                            {"key": "/siteserver/inc", "doc_count": 6},
                            {"key": "/css/album.css", "doc_count": 5},
                            {"key": "/.well-known/assetlinks.json", "doc_count": 4},
                            {"key": "/SiteServer/login.aspx", "doc_count": 4},
                            {"key": "/d/js", "doc_count": 3},
                        ],
                    },
                },
                {
                    "key": "403",
                    "doc_count": 434,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 309,
                        "buckets": [
                            {"key": "/goods/TECY07.html", "doc_count": 5},
                            {"key": "/pgoods/ECSBYY.html", "doc_count": 5},
                            {
                                "key": "/search/06,29-0601-------------1-4---.html",
                                "doc_count": 5,
                            },
                            {
                                "key": "/search/07%252C11%252C35%252C41-1110%252C1111------------2-4-2.html",
                                "doc_count": 5,
                            },
                            {
                                "key": "/search/30,37-3011-%25E6%2596%25B9%25E4%25BE%25BF%25E9%25A3%259F%25E5%2593%2581-7----3-------1-.html",
                                "doc_count": 4,
                            },
                            {"key": "/cgoods/R9XGDKCM98GM.html", "doc_count": 3},
                            {"key": "/pgoods/2W5TYY.html", "doc_count": 3},
                            {"key": "/pgoods/TS2TYY.html", "doc_count": 3},
                            {
                                "key": "/search/04-0403--6-----4----1--1-",
                                "doc_count": 3,
                            },
                            {
                                "key": "/search/35--------------2-2---.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/search/43--------------13---1-.html",
                                "doc_count": 3,
                            },
                            {"key": "/cgoods/DYNANASZU0KM.html", "doc_count": 2},
                            {"key": "/cgoods/P0A4W0QDHAXT.html", "doc_count": 2},
                            {"key": "/cgoods/S8RKU8QU085M.html", "doc_count": 2},
                            {"key": "/consulte/2-21-7487.html", "doc_count": 2},
                            {"key": "/consulte/2-23-1299%20.html", "doc_count": 2},
                            {"key": "/goods/1803711664.html", "doc_count": 2},
                            {"key": "/goods/2075050026.html", "doc_count": 2},
                            {"key": "/goods/2110195597.html", "doc_count": 2},
                            {"key": "/goods/2A67729A38D422.html", "doc_count": 2},
                        ],
                    },
                },
                {
                    "key": "304",
                    "doc_count": 49,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "/static/api", "doc_count": 10},
                            {"key": "/public/js", "doc_count": 3},
                            {"key": "/chat/mark_business_pc.html", "doc_count": 2},
                            {"key": "/chat/yzzlzx.html", "doc_count": 1},
                        ],
                    },
                },
                {
                    "key": "206",
                    "doc_count": 8,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "/public/error404", "doc_count": 8}],
                    },
                },
            ],
        },
        "city": {
            "doc_count_error_upper_bound": 643,
            "sum_other_doc_count": 49714,
            "buckets": [
                {
                    "key": "Beijing",
                    "doc_count": 886646,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 886646, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "wpT4-owB043sXHpDINtC",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Boydton",
                    "doc_count": 153291,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 153291, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "aQ9dC40BZnyrIs2wbvdu",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Hangzhou",
                    "doc_count": 123472,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 123472, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "ZQVcC40B043sXHpDybI9",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Ashburn",
                    "doc_count": 104731,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 104731, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "cEzvGY0BZnyrIs2wsMfI",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Chengdu",
                    "doc_count": 63478,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 63478, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "wniPFY0BZnyrIs2wqAqd",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Sichuan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shenzhen",
                    "doc_count": 58176,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 58176, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "kSdgAI0B043sXHpDBqbW",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Guangzhou",
                    "doc_count": 52888,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 52888, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "IqQA-4wBZnyrIs2wSOdB",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shanghai",
                    "doc_count": 41278,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 41278, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "YA5dC40BZnyrIs2wL-8b",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shanghai",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Nanjing",
                    "doc_count": 28777,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 28777, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "xUbeGY0BZnyrIs2wuDK4",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Jiangsu",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Zhengzhou",
                    "doc_count": 8641,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 8641, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "_keGAI0B043sXHpDIXUR",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Xiamen",
                    "doc_count": 3660,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3660, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "QOlvEY0BZnyrIs2w07BT",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Fujian",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Suzhou",
                    "doc_count": 3599,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3599, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "zqXGFY0BZnyrIs2wl5Gj",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Jiangsu",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Wuhan",
                    "doc_count": 3465,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3465, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "khrqAY0B043sXHpD_KT5",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Hubei",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Jinhua",
                    "doc_count": 3389,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3389, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "4GzBBY0BZnyrIs2wd24n",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Taizhou",
                    "doc_count": 3185,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3185, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "zGIpCY0B043sXHpDQ8a9",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Jiangsu",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Yiwu",
                    "doc_count": 2957,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2957, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "U9gCFY0BZnyrIs2wnbYf",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Quanzhou",
                    "doc_count": 2914,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2914, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "MCk7Fo0B043sXHpDfCYM",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Fujian",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Chongqing",
                    "doc_count": 2829,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2829, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "Fiqh_IwBZnyrIs2wixda",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Chongqing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Jining",
                    "doc_count": 2700,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2700, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "tPhvEI0B043sXHpDMVcq",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shandong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Changsha",
                    "doc_count": 2646,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2646, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "SjXKEI0B043sXHpDXiCn",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Hunan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "clientip": {
            "doc_count_error_upper_bound": 8785,
            "sum_other_doc_count": 1457485,
            "buckets": [
                {
                    "key": "121.41.74.221",
                    "doc_count": 112053,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 112053, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "Aj-FC40B043sXHpDIRvM",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "106.46.2.187",
                    "doc_count": 42745,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 42745, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "xdP9FY0B043sXHpDhlON",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.16.104",
                    "doc_count": 35832,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 35832, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "eITZ_owBZnyrIs2w5-ZF",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.20.235",
                    "doc_count": 31618,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 31618, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "DGsoCY0BZnyrIs2w8Zpm",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "3.224.220.101",
                    "doc_count": 27835,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 27835, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "8kfgGY0BZnyrIs2wLALA",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "52.70.240.171",
                    "doc_count": 27713,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 27713, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "OAkfAI0BZnyrIs2wl7Xg",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "23.22.35.162",
                    "doc_count": 27116,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 27116, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "xvZhEI0BZnyrIs2wzosV",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.17.176",
                    "doc_count": 25603,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 25603, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "sPmj_YwBZnyrIs2wfi1G",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.22.18",
                    "doc_count": 19192,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 19192, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "aFlPAo0B043sXHpDDCnj",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.19.189",
                    "doc_count": 18977,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 18977, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "hMxOAY0BZnyrIs2wZPf4",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.18.158",
                    "doc_count": 18801,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 18801, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "VEBTBY0B043sXHpDfYBr",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.16.158",
                    "doc_count": 18488,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 18488, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "G2u2AI0B043sXHpDnp9e",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.21.93",
                    "doc_count": 16596,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 16596, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "s5XLAo0BZnyrIs2w74oM",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.67",
                    "doc_count": 16036,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 16036, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "0klQBY0BZnyrIs2wyUFv",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.21.186",
                    "doc_count": 15175,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 15175, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "z2MqCY0B043sXHpDZBGS",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.32",
                    "doc_count": 14807,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 14807, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "gO5hEI0B043sXHpD0cHx",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.16.46",
                    "doc_count": 14684,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 14684, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "Jp3iAo0BZnyrIs2wVLmK",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.22.239",
                    "doc_count": 14343,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 14343, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "4hWZ_IwB043sXHpDuSuv",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "114.250.22.176",
                    "doc_count": 14310,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 14310, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "2Zz6AI0B043sXHpDNaq-",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "221.216.52.136",
                    "doc_count": 14168,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 14168, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "zxbSAY0BZnyrIs2wZNGU",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "day": {
            "buckets": [
                {
                    "key_as_string": "2024-01-12",
                    "key": 1705017600000,
                    "doc_count": 552457,
                },
                {
                    "key_as_string": "2024-01-13",
                    "key": 1705104000000,
                    "doc_count": 418197,
                },
                {
                    "key_as_string": "2024-01-14",
                    "key": 1705190400000,
                    "doc_count": 344246,
                },
                {
                    "key_as_string": "2024-01-15",
                    "key": 1705276800000,
                    "doc_count": 206338,
                },
                {
                    "key_as_string": "2024-01-16",
                    "key": 1705363200000,
                    "doc_count": 189884,
                },
                {
                    "key_as_string": "2024-01-17",
                    "key": 1705449600000,
                    "doc_count": 233071,
                },
                {
                    "key_as_string": "2024-01-18",
                    "key": 1705536000000,
                    "doc_count": 39384,
                },
            ]
        },
    },
    {
        "key": "qy.xxxx.com",
        "doc_count": 721987,
        "path": {
            "doc_count_error_upper_bound": 123,
            "sum_other_doc_count": 501692,
            "buckets": [
                {
                    "key": "/ajax/show_static",
                    "doc_count": 38078,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 38056},
                            {"key": "499", "doc_count": 22},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07500000298023224,
                            "95.0": 0.08133120499777358,
                            "99.0": 1.4359999895095825,
                        }
                    },
                },
                {
                    "key": "/Ajax/gethistory",
                    "doc_count": 24266,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 24251},
                            {"key": "499", "doc_count": 14},
                            {"key": "502", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07800000160932541,
                            "95.0": 1.3762311436900592,
                            "99.0": 1.8311451512745454,
                        }
                    },
                },
                {
                    "key": "/BuryingPoint/record",
                    "doc_count": 5590,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 5127},
                            {"key": "499", "doc_count": 463},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.11800000071525574,
                            "95.0": 0.12200000137090683,
                            "99.0": 0.13199999928474426,
                        }
                    },
                },
                {
                    "key": "/ajax/amhSearch",
                    "doc_count": 2487,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 2482},
                            {"key": "499", "doc_count": 5},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07199999690055847,
                            "95.0": 0.07500000298023224,
                            "99.0": 0.08062999948859226,
                        }
                    },
                },
                {
                    "key": "/ajax/flashCacheHtml",
                    "doc_count": 2030,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 2029},
                            {"key": "499", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07416666795810063,
                            "95.0": 0.07800000160932541,
                            "99.0": 1.4465999841690065,
                        }
                    },
                },
                {
                    "key": "/ajax/getBannerMenusHtmlNew",
                    "doc_count": 2030,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 2027},
                            {"key": "499", "doc_count": 3},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.4402500092983246,
                            "95.0": 0.6290000081062317,
                            "99.0": 1.9972000598907473,
                        }
                    },
                },
                {
                    "key": "/ajax/getGoodsQyDetailEvent",
                    "doc_count": 1872,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 1868},
                            {"key": "499", "doc_count": 4},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.1456571400165558,
                            "95.0": 0.22280000448226903,
                            "99.0": 0.30855999112129207,
                        }
                    },
                },
                {
                    "key": "/public/error404",
                    "doc_count": 1563,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 1559},
                            {"key": "206", "doc_count": 4},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.2035199546813966,
                            "95.0": 1.606283342838287,
                            "99.0": 2.410620031356809,
                        }
                    },
                },
                {
                    "key": "/qualification/s----------------1--1-1.html",
                    "doc_count": 1483,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 1480},
                            {"key": "499", "doc_count": 3},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.5665333191553752,
                            "95.0": 0.6018999993801116,
                            "99.0": 0.7306899905204778,
                        }
                    },
                },
                {
                    "key": "/ajax/areas",
                    "doc_count": 1309,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 1309}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.08383999854326254,
                            "95.0": 0.0860000029206276,
                            "99.0": 0.09099999815225601,
                        }
                    },
                },
                {
                    "key": "/commission/qualification.html",
                    "doc_count": 456,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 451},
                            {"key": "499", "doc_count": 5},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.6349999904632568,
                            "95.0": 0.6576999962329865,
                            "99.0": 2.596640067100524,
                        }
                    },
                },
                {
                    "key": "/AssignPrincipal/run",
                    "doc_count": 432,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 432}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.10999999940395355,
                            "95.0": 0.11299999803304672,
                            "99.0": 0.12117999970912934,
                        }
                    },
                },
                {
                    "key": "/search/s---2-------------1---1.html",
                    "doc_count": 423,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 423}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.5680000185966492,
                            "95.0": 0.5873500078916549,
                            "99.0": 0.6670800107717514,
                        }
                    },
                },
                {
                    "key": "/searchNew/searchByKeyword_wp",
                    "doc_count": 335,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 333},
                            {"key": "499", "doc_count": 2},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.38199999928474426,
                            "95.0": 0.4177500084042549,
                            "99.0": 0.6639499723911186,
                        }
                    },
                },
                {
                    "key": "/public/js",
                    "doc_count": 288,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 288}],
                    },
                    "time": {"values": {"90.0": 0.0, "95.0": 0.0, "99.0": 0.0}},
                },
                {
                    "key": "/ajax/getGoodsQyAptitudeDetailEvent",
                    "doc_count": 271,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 271}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.15540000200271606,
                            "95.0": 0.25190000385046,
                            "99.0": 0.3577100017666827,
                        }
                    },
                },
                {
                    "key": "/BuryingPoint/click",
                    "doc_count": 264,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 264}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.16709999591112135,
                            "95.0": 0.17130000442266463,
                            "99.0": 0.38436000704765627,
                        }
                    },
                },
                {
                    "key": "/search/s---1-------------1---1.html",
                    "doc_count": 141,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 141}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.5770000219345093,
                            "95.0": 0.600900012254715,
                            "99.0": 0.8352399826049847,
                        }
                    },
                },
                {
                    "key": "/Ajax/savehistory",
                    "doc_count": 119,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 119}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.0729999989271164,
                            "95.0": 0.07599999755620956,
                            "99.0": 0.09682000353932385,
                        }
                    },
                },
                {
                    "key": "/ajax/add_type_search_keyword",
                    "doc_count": 118,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 118}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.08500000089406967,
                            "95.0": 0.08759999871253966,
                            "99.0": 0.09396000176668165,
                        }
                    },
                },
            ],
        },
        "code": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "200",
                    "doc_count": 707045,
                    "path": {
                        "doc_count_error_upper_bound": 117,
                        "sum_other_doc_count": 487604,
                        "buckets": [
                            {"key": "/ajax/show_static", "doc_count": 38056},
                            {"key": "/Ajax/gethistory", "doc_count": 24251},
                            {"key": "/BuryingPoint/record", "doc_count": 5127},
                            {"key": "/ajax/amhSearch", "doc_count": 2482},
                            {"key": "/ajax/flashCacheHtml", "doc_count": 2029},
                            {"key": "/ajax/getBannerMenusHtmlNew", "doc_count": 2027},
                            {"key": "/ajax/getGoodsQyDetailEvent", "doc_count": 1868},
                            {"key": "/public/error404", "doc_count": 1559},
                            {
                                "key": "/qualification/s----------------1--1-1.html",
                                "doc_count": 1480,
                            },
                            {"key": "/ajax/areas", "doc_count": 1309},
                            {"key": "/commission/qualification.html", "doc_count": 451},
                            {"key": "/AssignPrincipal/run", "doc_count": 432},
                            {
                                "key": "/search/s---2-------------1---1.html",
                                "doc_count": 423,
                            },
                            {"key": "/searchNew/searchByKeyword_wp", "doc_count": 333},
                            {"key": "/public/js", "doc_count": 288},
                            {
                                "key": "/ajax/getGoodsQyAptitudeDetailEvent",
                                "doc_count": 271,
                            },
                            {"key": "/BuryingPoint/click", "doc_count": 264},
                            {
                                "key": "/search/s---1-------------1---1.html",
                                "doc_count": 141,
                            },
                            {"key": "/Ajax/savehistory", "doc_count": 123},
                            {"key": "/ajax/add_type_search_keyword", "doc_count": 118},
                        ],
                    },
                },
                {
                    "key": "302",
                    "doc_count": 8437,
                    "path": {
                        "doc_count_error_upper_bound": 21,
                        "sum_other_doc_count": 8158,
                        "buckets": [
                            {
                                "key": "/goods/0400A53J23340300412DM000.html",
                                "doc_count": 15,
                            },
                            {"key": "/goods/d8bkyy.html", "doc_count": 15},
                            {"key": "/goods/2Z7JYY.html", "doc_count": 13},
                            {"key": "/goods/D4YPYY.html", "doc_count": 13},
                            {"key": "/goods/EAB3697G26S589.html", "doc_count": 13},
                            {
                                "key": "/goods/TP00A8PK91550300478JF000.html",
                                "doc_count": 13,
                            },
                            {"key": "/goods/HK9KYY.html", "doc_count": 11},
                            {"key": "/goods/K8EKYY.html", "doc_count": 11},
                            {"key": "/goods/Y6CPYY.html", "doc_count": 10},
                            {
                                "key": "/goods/1N00A9XR65340300885QS000.html",
                                "doc_count": 9,
                            },
                            {
                                "key": "/goods/7000AWCB72820300332SY000.html",
                                "doc_count": 9,
                            },
                            {"key": "/goods/B2BPYY.html", "doc_count": 9},
                            {
                                "key": "/goods/C200A6W483130300297P0000.html",
                                "doc_count": 9,
                            },
                            {
                                "key": "/goods/KF00AHN689940300298HY000.html",
                                "doc_count": 9,
                            },
                            {
                                "key": "/goods/Q700A3HF09350300603H4000.html",
                                "doc_count": 9,
                            },
                            {
                                "key": "/goods/UT00AK3345450300024S1000.html",
                                "doc_count": 9,
                            },
                            {
                                "key": "/goods/W300A7CA78540300956AZ000.html",
                                "doc_count": 9,
                            },
                            {
                                "key": "/search/s--1--------------1--1.html",
                                "doc_count": 9,
                            },
                            {"key": "/goods/9389637308.html", "doc_count": 8},
                            {
                                "key": "/goods/GC00A2DH21530300036R5000.html",
                                "doc_count": 8,
                            },
                        ],
                    },
                },
                {
                    "key": "499",
                    "doc_count": 5454,
                    "path": {
                        "doc_count_error_upper_bound": 13,
                        "sum_other_doc_count": 4721,
                        "buckets": [
                            {"key": "/BuryingPoint/record", "doc_count": 463},
                            {
                                "key": "/qualification/s-%E5%8A%B3%E5%8A%A1%E8%B5%84%E8%B4%A8%E5%88%86%E5%8C%85---------------1--1-1.html",
                                "doc_count": 46,
                            },
                            {
                                "key": "/qualification/s-%E6%96%BD%E5%B7%A5%E6%80%BB%E6%89%BF%E5%8C%85---------------1--1-1.html",
                                "doc_count": 45,
                            },
                            {"key": "/ajax/show_static", "doc_count": 21},
                            {"key": "/Ajax/gethistory", "doc_count": 13},
                            {"key": "/commission/detail", "doc_count": 13},
                            {"key": "/ajax/amhSearch", "doc_count": 4},
                            {"key": "/ajax/getGoodsQyDetailEvent", "doc_count": 4},
                            {
                                "key": "/qualification/s--------------207600000000000138--1--1-1.html",
                                "doc_count": 4,
                            },
                            {"key": "/ajax/getBannerMenusHtmlNew", "doc_count": 3},
                            {
                                "key": "/aptitude/0200A0D506580300305WJ000.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/aptitude/2400A28Y23680300828RC000.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/aptitude/3002ANYY55461401977ZY768.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/aptitude/6Q00AHYY07651401332CY554.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/aptitude/8E01AHYY95151401303JY988.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/aptitude/EH00ABJS31660300314HT000.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/aptitude/G600ABYY97091401246GY942.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/aptitude/QW00AT2Y10980300100BY000.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/aptitude/UX00AGKC18330300257WY000.html",
                                "doc_count": 3,
                            },
                            {
                                "key": "/aptitude/UY01A4YY05231401482NY000.html",
                                "doc_count": 3,
                            },
                        ],
                    },
                },
                {
                    "key": "404",
                    "doc_count": 584,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 85,
                        "buckets": [
                            {"key": "/qy/djztc.html", "doc_count": 36},
                            {"key": "/help/question.html", "doc_count": 30},
                            {"key": "/admin/privilege.php", "doc_count": 18},
                            {"key": "/qy/logout", "doc_count": 18},
                            {"key": "/qy/lwpqxkz.html", "doc_count": 18},
                            {"key": "/qy/xgmnsrsj.html", "doc_count": 18},
                            {"key": "/zb_system/login.php", "doc_count": 18},
                            {"key": "/admin/login.php", "doc_count": 16},
                            {"key": "/dede/login.php", "doc_count": 16},
                            {"key": "/e/admin", "doc_count": 16},
                            {"key": "/css/modules", "doc_count": 15},
                            {"key": "/include/ckeditor", "doc_count": 15},
                            {"key": "/api/cart.html", "doc_count": 12},
                            {"key": "/plus/ad_js.php", "doc_count": 12},
                            {"key": "/plus/flink_add.php", "doc_count": 12},
                            {"key": "/qy/gsbgfw.html", "doc_count": 12},
                            {"key": "/qy/rlzyfwxkz.html", "doc_count": 12},
                            {"key": "/qy/spxzfxcybapz.html", "doc_count": 12},
                            {"key": "/qy/wxhxpjyxkz.html", "doc_count": 12},
                            {"key": "/qy/ylqxelbaxkz.html", "doc_count": 12},
                        ],
                    },
                },
                {
                    "key": "502",
                    "doc_count": 238,
                    "path": {
                        "doc_count_error_upper_bound": 3,
                        "sum_other_doc_count": 214,
                        "buckets": [
                            {
                                "key": "/aptitude/X801A6YY79241401137NY065.html",
                                "doc_count": 4,
                            },
                            {"key": "/Ajax/gethistory", "doc_count": 1},
                            {
                                "key": "/aptitude/0900AY8K36150300314GJ000.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/1P01ALYY44371401150EY248.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/3A01APYY62001403360TY026.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/4B01A4YY33071401360EY826.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/5J00ANC141900300305G5000.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/5X01APYY22381400360DY355.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/7001A3YY05331401489XY618.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/7Z00AM8084820300259WF000.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/A801A6YY15151401899TY955.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/BF01ABYY96101401100PY223.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/DT01APYY91001401479RY226.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/EF00AUKW52920300623JA000.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/EJ02A4YY17871400360AY537.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/GF00ASS828610300985DU000.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/H504A2YY76261401332MY456.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/K100ATQJ45620300259EQ000.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/MS02A4YY19511401360CY287.html",
                                "doc_count": 1,
                            },
                            {
                                "key": "/aptitude/UP00ABRT55080300100BX000.html",
                                "doc_count": 1,
                            },
                        ],
                    },
                },
                {
                    "key": "301",
                    "doc_count": 218,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 152,
                        "buckets": [
                            {"key": "/consulte/3-15579.html", "doc_count": 7},
                            {"key": "/consulte/3-15837.html", "doc_count": 7},
                            {"key": "/consulte/3-16497.html", "doc_count": 6},
                            {"key": "/consulte/3-16592.html", "doc_count": 6},
                            {"key": "/consulte/3-16033.html", "doc_count": 4},
                            {"key": "/consulte/3-17160.html", "doc_count": 4},
                            {"key": "/consulte/3-277-8.html", "doc_count": 4},
                            {"key": "/consulte/3-16692.html", "doc_count": 3},
                            {"key": "/consulte/3-15630.html", "doc_count": 2},
                            {"key": "/consulte/3-15780.html", "doc_count": 2},
                            {"key": "/consulte/3-15892.html", "doc_count": 2},
                            {"key": "/consulte/3-16126.html", "doc_count": 2},
                            {"key": "/consulte/3-16593.html", "doc_count": 2},
                            {"key": "/consulte/3-16668.html", "doc_count": 2},
                            {"key": "/consulte/3-16785.html", "doc_count": 2},
                            {"key": "/consulte/3-16821.html", "doc_count": 2},
                            {"key": "/consulte/3-16823.html", "doc_count": 2},
                            {"key": "/consulte/3-16916.html", "doc_count": 2},
                            {"key": "/consulte/3-17002.html", "doc_count": 2},
                            {"key": "/consulte/3-17174.html", "doc_count": 2},
                        ],
                    },
                },
                {
                    "key": "206",
                    "doc_count": 6,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "/public/error404", "doc_count": 4}],
                    },
                },
                {
                    "key": "304",
                    "doc_count": 3,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [],
                    },
                },
                {
                    "key": "403",
                    "doc_count": 2,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "/goods/HA8G492G75M102.ht", "doc_count": 1},
                            {"key": "/goods/ZA8E492U90S406.ht", "doc_count": 1},
                        ],
                    },
                },
            ],
        },
        "city": {
            "doc_count_error_upper_bound": 50,
            "sum_other_doc_count": 5471,
            "buckets": [
                {
                    "key": "New York",
                    "doc_count": 175477,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 175477, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "69P9FY0B043sXHpDfEga",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "New York",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Boydton",
                    "doc_count": 155063,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 155063, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "w0DeGY0B043sXHpDuTEm",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Hangzhou",
                    "doc_count": 67212,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 67212, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "Odr9FY0BZnyrIs2wwhm7",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Ashburn",
                    "doc_count": 21701,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 21701, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "RiVdAI0B043sXHpDgU71",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Chengdu",
                    "doc_count": 8450,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 8450, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "Xm_tBY0B043sXHpDj-Ed",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Sichuan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Beijing",
                    "doc_count": 6995,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 6995, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "zP1rEI0BZnyrIs2wGpdu",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shenzhen",
                    "doc_count": 6512,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 6512, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "UHAGEY0B043sXHpD9Lts",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shanghai",
                    "doc_count": 4149,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 4149, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "Bk1gBY0BZnyrIs2w8Rd3",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shanghai",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Zhengzhou",
                    "doc_count": 3835,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3835, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "kUfoCo0BZnyrIs2w2BHX",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Bochum",
                    "doc_count": 3196,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3196, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "LkDeGY0B043sXHpDrSrf",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "Germany",
                                            "region_name": "North Rhine-Westphalia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Guangzhou",
                    "doc_count": 1880,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1880, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "S5qABo0B043sXHpDZksp",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Wuhan",
                    "doc_count": 492,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 492, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "8AdbBI0BZnyrIs2wRTdN",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Hubei",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Fuzhou",
                    "doc_count": 436,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 436, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "FOxVC40B043sXHpDlvu0",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Fujian",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Wuxi",
                    "doc_count": 435,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 435, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "GUVkF40B043sXHpDl24O",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Jiangsu",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Xi'an",
                    "doc_count": 321,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 321, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "IDScD40B043sXHpDcl-d",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Jinan",
                    "doc_count": 250,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 250, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "Um6n_owBZnyrIs2wdB4E",
                                    "_score": 2.0,
                                    "_ignored": ["UA.keyword"],
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shandong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Kunming",
                    "doc_count": 241,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 241, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "PngrGo0B043sXHpDpnkR",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Yunnan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Xiamen",
                    "doc_count": 238,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 238, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "da8iAY0B043sXHpDrmYe",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Fujian",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Qingdao",
                    "doc_count": 237,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 237, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "rFiEBY0BZnyrIs2wwOYM",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shandong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Nanning",
                    "doc_count": 235,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 235, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "_G66AI0B043sXHpDGYoq",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "clientip": {
            "doc_count_error_upper_bound": 1862,
            "sum_other_doc_count": 372457,
            "buckets": [
                {
                    "key": "47.76.35.19",
                    "doc_count": 175477,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 175477, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "zhSZ_IwB043sXHpDKaAu",
                                    "_score": 2.0,
                                    "_ignored": [
                                        "request_uri.keyword",
                                        "path_2nd.keyword",
                                        "url.keyword",
                                    ],
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "New York",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "121.41.74.221",
                    "doc_count": 58684,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 58684, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "h2OkBY0BZnyrIs2wj8pO",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "162.55.85.223",
                    "doc_count": 25602,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 25602, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "H8ZrGI0B043sXHpDJtvY",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "Germany"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.98",
                    "doc_count": 18495,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 18495, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "rTIzDI0B043sXHpDI12i",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.54",
                    "doc_count": 17236,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 17236, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "ySLHBI0BZnyrIs2wJ5Lm",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.88",
                    "doc_count": 16676,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 16676, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "oNP9FY0B043sXHpD5eFX",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "52.167.144.145",
                    "doc_count": 3848,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3848, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "3enNC40B043sXHpDrxMC",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "212.227.175.149",
                    "doc_count": 3196,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3196, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "0EbvGY0B043sXHpDq8XP",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "Germany",
                                            "region_name": "North Rhine-Westphalia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "52.167.144.228",
                    "doc_count": 2948,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2948, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "SUlRBY0BZnyrIs2wy5pY",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "40.77.167.247",
                    "doc_count": 2927,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2927, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "XGi1BY0BZnyrIs2wGo0K",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "40.77.167.52",
                    "doc_count": 2870,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2870, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "vK7TFY0BZnyrIs2wLGOM",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "52.167.144.238",
                    "doc_count": 2763,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2763, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "qvNr_IwBZnyrIs2wmOZK",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "40.77.167.22",
                    "doc_count": 2660,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2660, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "ZE0AGo0B043sXHpDWhfN",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "120.78.222.64",
                    "doc_count": 2624,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2624, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "oERjBY0B043sXHpDfEhN",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "52.167.144.219",
                    "doc_count": 2587,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2587, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "0JrRFI0B043sXHpD37nR",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "40.77.167.53",
                    "doc_count": 2297,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2297, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "G0pXBY0BZnyrIs2wP980",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "40.77.167.136",
                    "doc_count": 2236,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2236, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "zWfSBY0B043sXHpDFKKG",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "52.167.144.140",
                    "doc_count": 2225,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2225, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "gj7B_IwB043sXHpDU5pn",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "40.77.167.50",
                    "doc_count": 2177,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2177, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "1z14AI0B043sXHpDuidE",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "52.167.144.214",
                    "doc_count": 2002,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2002, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "gJC0FY0B043sXHpDaVXI",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "day": {
            "buckets": [
                {
                    "key_as_string": "2024-01-12",
                    "key": 1705017600000,
                    "doc_count": 150514,
                },
                {
                    "key_as_string": "2024-01-13",
                    "key": 1705104000000,
                    "doc_count": 138406,
                },
                {
                    "key_as_string": "2024-01-14",
                    "key": 1705190400000,
                    "doc_count": 83228,
                },
                {
                    "key_as_string": "2024-01-15",
                    "key": 1705276800000,
                    "doc_count": 105450,
                },
                {
                    "key_as_string": "2024-01-16",
                    "key": 1705363200000,
                    "doc_count": 86069,
                },
                {
                    "key_as_string": "2024-01-17",
                    "key": 1705449600000,
                    "doc_count": 143776,
                },
                {
                    "key_as_string": "2024-01-18",
                    "key": 1705536000000,
                    "doc_count": 14544,
                },
            ]
        },
    },
    {
        "key": "mj.yuzhua.com",
        "doc_count": 353408,
        "path": {
            "doc_count_error_upper_bound": 57,
            "sum_other_doc_count": 340726,
            "buckets": [
                {
                    "key": "/ajax/show_static",
                    "doc_count": 2172,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 2157},
                            {"key": "499", "doc_count": 15},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07699999958276749,
                            "95.0": 0.0860000029206276,
                            "99.0": 1.435460016727449,
                        }
                    },
                },
                {
                    "key": "/BuryingPoint/record",
                    "doc_count": 931,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 802},
                            {"key": "499", "doc_count": 129},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.0689999982714653,
                            "95.0": 0.07100000232458115,
                            "99.0": 1.3999500477313993,
                        }
                    },
                },
                {
                    "key": "/ajax/show_static.html",
                    "doc_count": 651,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 648},
                            {"key": "499", "doc_count": 3},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07259999811649322,
                            "95.0": 0.07500000298023224,
                            "99.0": 1.2561300322413533,
                        }
                    },
                },
                {
                    "key": "/public/error404",
                    "doc_count": 628,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 627},
                            {"key": "499", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.1407999753952027,
                            "95.0": 1.6422000527381904,
                            "99.0": 2.3880399894714435,
                        }
                    },
                },
                {
                    "key": "/search/3.html",
                    "doc_count": 316,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 283},
                            {"key": "302", "doc_count": 31},
                            {"key": "499", "doc_count": 2},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.746199977397919,
                            "95.0": 2.00850007534027,
                            "99.0": 3.1461400604248,
                        }
                    },
                },
                {
                    "key": "/search/1.html",
                    "doc_count": 200,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 187},
                            {"key": "302", "doc_count": 12},
                            {"key": "499", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.6489999890327454,
                            "95.0": 1.7509999871253967,
                            "99.0": 2.1045000553131104,
                        }
                    },
                },
                {
                    "key": "/public/js",
                    "doc_count": 153,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 152},
                            {"key": "404", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.0,
                            "95.0": 0.0,
                            "99.0": 0.0010000000474974513,
                        }
                    },
                },
                {
                    "key": "/CountTrade/every_hours",
                    "doc_count": 147,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 147}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.06400000303983688,
                            "95.0": 0.06700000166893005,
                            "99.0": 0.06935000352561478,
                        }
                    },
                },
                {
                    "key": "/ajax/getIndexOtherData",
                    "doc_count": 145,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 136},
                            {"key": "499", "doc_count": 9},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.934999942779541,
                            "95.0": 2.2394999265670776,
                            "99.0": 3.611800074577344,
                        }
                    },
                },
                {
                    "key": "/ajax/getGoodsDetailInfo",
                    "doc_count": 133,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 133}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.14000000059604645,
                            "95.0": 0.14285000637173653,
                            "99.0": 0.1605099974572658,
                        }
                    },
                },
                {
                    "key": "/search/2.html",
                    "doc_count": 133,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 130},
                            {"key": "302", "doc_count": 3},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.682200026512146,
                            "95.0": 1.7130000591278076,
                            "99.0": 1.969679993391037,
                        }
                    },
                },
                {
                    "key": "/help/question.html",
                    "doc_count": 93,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "404", "doc_count": 93}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.01899999938905239,
                            "95.0": 0.01899999938905239,
                            "99.0": 0.026000000536441803,
                        }
                    },
                },
                {
                    "key": "/BuryingPoint/click",
                    "doc_count": 88,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 86},
                            {"key": "499", "doc_count": 2},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.07100000232458115,
                            "95.0": 0.07999999821186066,
                            "99.0": 0.863339975327259,
                        }
                    },
                },
                {
                    "key": "/consulte/2-204-47640.html",
                    "doc_count": 85,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "302", "doc_count": 64},
                            {"key": "200", "doc_count": 21},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 2.010999917984009,
                            "95.0": 2.0584999322891235,
                            "99.0": 2.4524000525474556,
                        }
                    },
                },
                {
                    "key": "/mj/_nuxt",
                    "doc_count": 44,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "404", "doc_count": 44}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.01899999938905239,
                            "95.0": 0.01899999938905239,
                            "99.0": 0.019999999552965164,
                        }
                    },
                },
                {
                    "key": "/consulte/2-20-40796.html",
                    "doc_count": 25,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "302", "doc_count": 21},
                            {"key": "200", "doc_count": 4},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.7049999833106995,
                            "95.0": 0.7974999994039536,
                            "99.0": 0.843999981880188,
                        }
                    },
                },
                {
                    "key": "/goods/6F01AEKY69551503179DY796.html",
                    "doc_count": 25,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "200", "doc_count": 25}],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.8020000457763672,
                            "95.0": 1.9455000460147858,
                            "99.0": 2.115000009536743,
                        }
                    },
                },
                {
                    "key": "/consulte/2-21-27189.html",
                    "doc_count": 23,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "302", "doc_count": 13},
                            {"key": "200", "doc_count": 10},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 2.2194000720977782,
                            "95.0": 2.7380499720573397,
                            "99.0": 3.624000072479248,
                        }
                    },
                },
                {
                    "key": "/search/4-------------4.html",
                    "doc_count": 21,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 19},
                            {"key": "302", "doc_count": 2},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.7466000080108643,
                            "95.0": 1.8618000447750092,
                            "99.0": 1.9190000295639038,
                        }
                    },
                },
                {
                    "key": "/consulte/1-20.html",
                    "doc_count": 20,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                            {"key": "200", "doc_count": 19},
                            {"key": "302", "doc_count": 1},
                        ],
                    },
                    "time": {
                        "values": {
                            "90.0": 1.298000007867813,
                            "95.0": 2.0419999957084656,
                            "99.0": 2.447999954223633,
                        }
                    },
                },
            ],
        },
        "code": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "200",
                    "doc_count": 342408,
                    "path": {
                        "doc_count_error_upper_bound": 42,
                        "sum_other_doc_count": 330533,
                        "buckets": [
                            {"key": "/ajax/show_static", "doc_count": 2157},
                            {"key": "/BuryingPoint/record", "doc_count": 802},
                            {"key": "/ajax/show_static.html", "doc_count": 648},
                            {"key": "/public/error404", "doc_count": 627},
                            {"key": "/search/3.html", "doc_count": 283},
                            {"key": "/search/1.html", "doc_count": 189},
                            {"key": "/public/js", "doc_count": 152},
                            {"key": "/CountTrade/every_hours", "doc_count": 147},
                            {"key": "/ajax/getIndexOtherData", "doc_count": 138},
                            {"key": "/ajax/getGoodsDetailInfo", "doc_count": 136},
                            {"key": "/search/2.html", "doc_count": 130},
                            {"key": "/BuryingPoint/click", "doc_count": 90},
                            {
                                "key": "/goods/6F01AEKY69551503179DY796.html",
                                "doc_count": 28,
                            },
                            {"key": "/consulte/1-22.html", "doc_count": 27},
                            {"key": "/consulte/1-21.html", "doc_count": 22},
                            {"key": "/consulte/1-20.html", "doc_count": 21},
                            {
                                "key": "/goods/112176509614361157327.html",
                                "doc_count": 19,
                            },
                            {
                                "key": "/goods/LR02AHEY52961503296EY848.html",
                                "doc_count": 19,
                            },
                            {
                                "key": "/goods/RH00A3DT55890300307CF000.html",
                                "doc_count": 19,
                            },
                            {
                                "key": "/goods/KD00ASK983920300280K2000.html",
                                "doc_count": 18,
                            },
                        ],
                    },
                },
                {
                    "key": "302",
                    "doc_count": 6505,
                    "path": {
                        "doc_count_error_upper_bound": 23,
                        "sum_other_doc_count": 6142,
                        "buckets": [
                            {"key": "/consulte/2-204-47640.html", "doc_count": 63},
                            {"key": "/search/3.html", "doc_count": 24},
                            {"key": "/consulte/2-20-40796.html", "doc_count": 23},
                            {
                                "key": "/goods/YE00A7BL57010300307BA000.html",
                                "doc_count": 20,
                            },
                            {"key": "/consulte/2-20-32124.html", "doc_count": 18},
                            {"key": "/consulte/2-202-52910.html", "doc_count": 17},
                            {"key": "/consulte/2-22-321633.html", "doc_count": 16},
                            {"key": "/consulte/2-20-41294.html", "doc_count": 15},
                            {"key": "/consulte/2-21-27189.html", "doc_count": 15},
                            {"key": "/consulte/2-202-26239.html", "doc_count": 14},
                            {"key": "/consulte/2-21-26664.html", "doc_count": 14},
                            {"key": "/consulte/2-20-45080.html", "doc_count": 13},
                            {"key": "/consulte/2-20-16117.html", "doc_count": 12},
                            {"key": "/consulte/2-21-39830.html", "doc_count": 12},
                            {"key": "/consulte/2-20-26548.html", "doc_count": 10},
                            {"key": "/consulte/2-203-52056.html", "doc_count": 10},
                            {"key": "/search/1.html", "doc_count": 10},
                            {"key": "/consulte/2-204-52417.html", "doc_count": 9},
                            {"key": "/consulte/2-21-353714.html", "doc_count": 9},
                            {"key": "/consulte/2-21-40369.html", "doc_count": 9},
                        ],
                    },
                },
                {
                    "key": "499",
                    "doc_count": 2088,
                    "path": {
                        "doc_count_error_upper_bound": 9,
                        "sum_other_doc_count": 1851,
                        "buckets": [
                            {"key": "/BuryingPoint/record", "doc_count": 129},
                            {"key": "/ajax/show_static", "doc_count": 13},
                            {"key": "/ajax/getIndexOtherData", "doc_count": 8},
                            {
                                "key": "/goods/112115220306691858609.html",
                                "doc_count": 6,
                            },
                            {"key": "/search/1-3-------------1.html", "doc_count": 6},
                            {
                                "key": "/goods/119135742447219748295.html",
                                "doc_count": 5,
                            },
                            {"key": "/search/2-------------19--3.html", "doc_count": 5},
                            {"key": "/search/1-1-------------1.html", "doc_count": 4},
                            {"key": "/search/1-14-------------3.html", "doc_count": 4},
                            {"key": "/search/1-17-------------1.html", "doc_count": 4},
                            {"key": "/search/1-23-------------1.html", "doc_count": 4},
                            {"key": "/search/2-------------1--2.html", "doc_count": 4},
                            {"key": "/search/2-------------13--1.html", "doc_count": 4},
                            {"key": "/search/2-------------16--2.html", "doc_count": 4},
                            {"key": "/search/2-------------18--1.html", "doc_count": 4},
                            {"key": "/search/2-------------21--2.html", "doc_count": 4},
                            {"key": "/search/2-------------6--2.html", "doc_count": 4},
                            {"key": "/search/2-22--------------1.html", "doc_count": 4},
                            {"key": "/search/2-28--------------2.html", "doc_count": 4},
                            {"key": "/consulte/2-20-31912.html", "doc_count": 3},
                        ],
                    },
                },
                {
                    "key": "404",
                    "doc_count": 1307,
                    "path": {
                        "doc_count_error_upper_bound": 12,
                        "sum_other_doc_count": 631,
                        "buckets": [
                            {"key": "/help/question.html", "doc_count": 102},
                            {"key": "/mj/_nuxt", "doc_count": 44},
                            {"key": "/help/problem", "doc_count": 18},
                            {"key": "/consult/3-43.html", "doc_count": 17},
                            {"key": "/user/register.html", "doc_count": 16},
                            {"key": "/user/order", "doc_count": 11},
                            {"key": "/e/DoInfo", "doc_count": 10},
                            {"key": "/bbs/static", "doc_count": 9},
                            {"key": "/include/ckeditor", "doc_count": 9},
                            {"key": "/plus/ad_js.php", "doc_count": 7},
                            {"key": "/base/templates", "doc_count": 6},
                            {"key": "/city/zaozhuangershouleikesasi", "doc_count": 6},
                            {"key": "/consult/3-12.html", "doc_count": 6},
                            {"key": "/consult/3-188.html", "doc_count": 6},
                            {"key": "/consult/3-190.html", "doc_count": 6},
                            {"key": "/consult/3-299.html", "doc_count": 6},
                            {"key": "/consult/3-40.html", "doc_count": 6},
                            {"key": "/help/index", "doc_count": 6},
                            {
                                "key": "/http:/shddyjg.com.style.yuzhua.com",
                                "doc_count": 6,
                            },
                            {"key": "/static/image", "doc_count": 6},
                        ],
                    },
                },
                {
                    "key": "403",
                    "doc_count": 577,
                    "path": {
                        "doc_count_error_upper_bound": 3,
                        "sum_other_doc_count": 532,
                        "buckets": [
                            {"key": "/consulte/1-21-133.html", "doc_count": 1},
                            {"key": "/consulte/1-21-136.html", "doc_count": 1},
                            {"key": "/consulte/1-21-138.html", "doc_count": 1},
                            {"key": "/consulte/1-21-141.html", "doc_count": 1},
                            {"key": "/consulte/1-21-7.html", "doc_count": 1},
                            {"key": "/consulte/1-21-8.html", "doc_count": 1},
                            {"key": "/consulte/1-21-9.html", "doc_count": 1},
                            {"key": "/consulte/2-20-100695.html", "doc_count": 1},
                            {"key": "/consulte/2-20-100881.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101018.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101070.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101071.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101121.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101437.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101442.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101550.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101551.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101617.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101655.html", "doc_count": 1},
                            {"key": "/consulte/2-20-101712.html", "doc_count": 1},
                        ],
                    },
                },
                {
                    "key": "301",
                    "doc_count": 520,
                    "path": {
                        "doc_count_error_upper_bound": 1,
                        "sum_other_doc_count": 433,
                        "buckets": [
                            {"key": "/consulte/3-8590", "doc_count": 15},
                            {"key": "/consulte/3-5019-1.html", "doc_count": 6},
                            {"key": "/consulte/3-13167", "doc_count": 5},
                            {"key": "/consulte/3-5185-1.html", "doc_count": 5},
                            {"key": "/consulte/3-13585-1.html", "doc_count": 4},
                            {"key": "/consulte/3-18458-1.html", "doc_count": 4},
                            {"key": "/consulte/3-4594-1.html", "doc_count": 4},
                            {"key": "/consulte/3-4717", "doc_count": 4},
                            {"key": "/consulte/3-5261-1.html", "doc_count": 4},
                            {"key": "/consulte/3-5310-1.html", "doc_count": 4},
                            {"key": "/consulte/3-9984-1.html", "doc_count": 4},
                            {"key": "/consulte/3-15158", "doc_count": 3},
                            {"key": "/consulte/3-18291-1.html", "doc_count": 3},
                            {"key": "/consulte/3-3841-1.html", "doc_count": 3},
                            {"key": "/consulte/3-4070-1.html", "doc_count": 3},
                            {"key": "/consulte/3-4168", "doc_count": 3},
                            {"key": "/consulte/3-4312", "doc_count": 3},
                            {"key": "/consulte/3-5437-1.html", "doc_count": 3},
                            {"key": "/consulte/3-7935", "doc_count": 3},
                            {"key": "/consulte/3-8903-1.html", "doc_count": 3},
                        ],
                    },
                },
                {
                    "key": "304",
                    "doc_count": 3,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [],
                    },
                },
            ],
        },
        "city": {
            "doc_count_error_upper_bound": 18,
            "sum_other_doc_count": 2264,
            "buckets": [
                {
                    "key": "Shenzhen",
                    "doc_count": 4881,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 4881, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "zagK-4wBZnyrIs2wcq-c",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Hangzhou",
                    "doc_count": 3931,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3931, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "ttz_FY0BZnyrIs2w-OwG",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Zhejiang",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Beijing",
                    "doc_count": 3531,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3531, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "-EFXBY0B043sXHpDqpAH",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shanghai",
                    "doc_count": 2360,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2360, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "fJDOCY0BZnyrIs2wmLtD",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shanghai",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Boydton",
                    "doc_count": 2315,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2315, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "Q3EIEY0B043sXHpDEsZG",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Zhengzhou",
                    "doc_count": 824,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 824, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "DcRIEY0BZnyrIs2w6mbJ",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Henan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Chengdu",
                    "doc_count": 766,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 766, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "Vccz-4wBZnyrIs2wuKIR",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Sichuan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Guangzhou",
                    "doc_count": 689,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 689, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "bHm7AI0BZnyrIs2wBuyo",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Ashburn",
                    "doc_count": 569,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 569, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "WaZmEo0BZnyrIs2wKpKg",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Virginia",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Council Bluffs",
                    "doc_count": 327,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 327, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "p0fhGY0BZnyrIs2w95hV",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Iowa",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Jinan",
                    "doc_count": 205,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 205, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "1W_MBY0BZnyrIs2w36nm",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shandong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Shijiazhuang",
                    "doc_count": 188,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 188, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "Rl7rEI0BZnyrIs2wqw0t",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Hebei",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Xiamen",
                    "doc_count": 181,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 181, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "NsSGCo0BZnyrIs2wiHc0",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Fujian",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Riga",
                    "doc_count": 159,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 159, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "Y_fnFo0BZnyrIs2wncSv",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "Latvia",
                                            "region_name": "Riga",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Fuzhou",
                    "doc_count": 156,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 156, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "2_w0BI0BZnyrIs2wYFc3",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Fujian",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Helsinki",
                    "doc_count": 154,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 154, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "C2kiCY0BZnyrIs2wAlEk",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "Finland",
                                            "region_name": "Uusimaa",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Nanjing",
                    "doc_count": 154,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 154, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "GosqBo0BZnyrIs2w0NVz",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Jiangsu",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Hefei",
                    "doc_count": 139,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 139, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "fbBUGo0BZnyrIs2w5_pT",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Anhui",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Lu'an",
                    "doc_count": 130,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 130, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "-MdaGI0BZnyrIs2wyLlT",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Anhui",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Wuhan",
                    "doc_count": 119,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 119, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "cSPsBI0B043sXHpDZQY2",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Hubei",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "clientip": {
            "doc_count_error_upper_bound": 488,
            "sum_other_doc_count": 81383,
            "buckets": [
                {
                    "key": "64.124.8.77",
                    "doc_count": 69052,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 69052, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "GoolBo0BZnyrIs2wPT3X",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.90",
                    "doc_count": 67368,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 67368, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "DW0tCY0BZnyrIs2w0BMw",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.70",
                    "doc_count": 58675,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 58675, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "-zcxDI0BZnyrIs2wuNDC",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.39",
                    "doc_count": 51972,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 51972, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "-XYEEY0BZnyrIs2w-6BR",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "162.55.85.223",
                    "doc_count": 6233,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 6233, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "L3h-CY0B043sXHpDlk46",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "Germany"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "94.130.237.182",
                    "doc_count": 5038,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 5038, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "yI-4FI0B043sXHpDXXka",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "Germany"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "120.78.222.64",
                    "doc_count": 2938,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2938, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "FULlGY0B043sXHpDk92I",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "216.244.66.244",
                    "doc_count": 1635,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1635, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "r13R_IwBZnyrIs2wiSBo",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {"country_name": "United States"}
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.57",
                    "doc_count": 1416,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1416, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "uxBcGY0B043sXHpDS1zb",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.67",
                    "doc_count": 1162,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1162, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.17",
                                    "_type": "_doc",
                                    "_id": "ICiPGY0BZnyrIs2wD6iY",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "47.107.254.32",
                    "doc_count": 1029,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1029, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "ZVUGGo0BZnyrIs2wZamz",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.96",
                    "doc_count": 843,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 843, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "G3glGo0BZnyrIs2wYmRK",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "64.124.8.82",
                    "doc_count": 817,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 817, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.18",
                                    "_type": "_doc",
                                    "_id": "-kbeGY0BZnyrIs2wujUv",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "United States",
                                            "region_name": "Michigan",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "220.181.108.102",
                    "doc_count": 573,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 573, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "iDNhAI0BZnyrIs2wIMDo",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "220.181.108.84",
                    "doc_count": 557,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 557, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "4VGIBY0B043sXHpDoS8I",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "220.181.108.157",
                    "doc_count": 555,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 555, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "KNBVAY0BZnyrIs2wzJGT",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "220.181.108.112",
                    "doc_count": 550,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 550, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "JXbiBY0BZnyrIs2whQhs",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "220.181.108.103",
                    "doc_count": 541,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 541, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "JB93C40B043sXHpDbTd3",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "220.181.108.155",
                    "doc_count": 539,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 539, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.16",
                                    "_type": "_doc",
                                    "_id": "9xurEI0B043sXHpD1rHW",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "220.181.108.92",
                    "doc_count": 532,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 532, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.12",
                                    "_type": "_doc",
                                    "_id": "LLU2_IwB043sXHpDj5LF",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "day": {
            "buckets": [
                {
                    "key_as_string": "2024-01-12",
                    "key": 1705017600000,
                    "doc_count": 13948,
                },
                {
                    "key_as_string": "2024-01-13",
                    "key": 1705104000000,
                    "doc_count": 27608,
                },
                {
                    "key_as_string": "2024-01-14",
                    "key": 1705190400000,
                    "doc_count": 113076,
                },
                {
                    "key_as_string": "2024-01-15",
                    "key": 1705276800000,
                    "doc_count": 103720,
                },
                {
                    "key_as_string": "2024-01-16",
                    "key": 1705363200000,
                    "doc_count": 69414,
                },
                {
                    "key_as_string": "2024-01-17",
                    "key": 1705449600000,
                    "doc_count": 19303,
                },
                {
                    "key_as_string": "2024-01-18",
                    "key": 1705536000000,
                    "doc_count": 6339,
                },
            ]
        },
    },
    {
        "key": "r-clear-1.yuzhua.com",
        "doc_count": 1042,
        "path": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [],
        },
        "code": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "200",
                    "doc_count": 1038,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [],
                    },
                },
                {
                    "key": "403",
                    "doc_count": 4,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [],
                    },
                },
            ],
        },
        "city": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "Shenzhen",
                    "doc_count": 1029,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1029, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "z0x-AI0BZnyrIs2wd1Pc",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Beijing",
                    "doc_count": 3,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "3SLpBI0B043sXHpD_1Xn",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Xi'an",
                    "doc_count": 2,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 2, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "Cc2RA40B043sXHpDI2l8",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Xianyang",
                    "doc_count": 1,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "gMuPDo0B043sXHpDNa5f",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "clientip": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "47.107.254.32",
                    "doc_count": 1029,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1029, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "z0x-AI0BZnyrIs2wd1Pc",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "47.92.73.109",
                    "doc_count": 3,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "3SLpBI0B043sXHpD_1Xn",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "113.215.188.70",
                    "doc_count": 3,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "Oe0gBI0B043sXHpDDAS8",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "113.215.188.73",
                    "doc_count": 3,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "uC7zBI0BZnyrIs2ww5yA",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "1.82.239.13",
                    "doc_count": 1,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "Ld8NDY0BZnyrIs2wOe9Q",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "36.40.78.216",
                    "doc_count": 1,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "L0ETAo0BZnyrIs2wvhw7",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "113.137.35.210",
                    "doc_count": 1,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "Cc2RA40B043sXHpDI2l8",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "113.142.152.219",
                    "doc_count": 1,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "gMuPDo0B043sXHpDNa5f",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "day": {
            "buckets": [
                {"key_as_string": "2024-01-12", "key": 1705017600000, "doc_count": 168},
                {"key_as_string": "2024-01-13", "key": 1705104000000, "doc_count": 179},
                {"key_as_string": "2024-01-14", "key": 1705190400000, "doc_count": 168},
                {"key_as_string": "2024-01-15", "key": 1705276800000, "doc_count": 170},
                {"key_as_string": "2024-01-16", "key": 1705363200000, "doc_count": 168},
                {"key_as_string": "2024-01-17", "key": 1705449600000, "doc_count": 168},
                {"key_as_string": "2024-01-18", "key": 1705536000000, "doc_count": 21},
            ]
        },
    },
    {
        "key": "r-clear-2.xxxx.com",
        "doc_count": 1040,
        "path": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "/dist/images",
                    "doc_count": 1,
                    "code": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "404", "doc_count": 1}],
                    },
                    "time": {
                        "values": {
                            "90.0": 0.003000000026077032,
                            "95.0": 0.003000000026077032,
                            "99.0": 0.003000000026077032,
                        }
                    },
                }
            ],
        },
        "code": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "200",
                    "doc_count": 1034,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [],
                    },
                },
                {
                    "key": "403",
                    "doc_count": 4,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [],
                    },
                },
                {
                    "key": "404",
                    "doc_count": 1,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [{"key": "/dist/images", "doc_count": 1}],
                    },
                },
                {
                    "key": "499",
                    "doc_count": 1,
                    "path": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [],
                    },
                },
            ],
        },
        "city": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "Shenzhen",
                    "doc_count": 1029,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1029, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "_4ACBo0BZnyrIs2wOjGZ",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Beijing",
                    "doc_count": 4,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 4, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "5DV0CI0B043sXHpDC2OQ",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "Xi'an",
                    "doc_count": 3,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "-UIVAo0BZnyrIs2wCjbW",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "clientip": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "47.107.254.32",
                    "doc_count": 1029,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1029, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "_4ACBo0BZnyrIs2wOjGZ",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Guangdong",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "39.103.168.88",
                    "doc_count": 4,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 4, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.14",
                                    "_type": "_doc",
                                    "_id": "5DV0CI0B043sXHpDC2OQ",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Beijing",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "113.215.188.70",
                    "doc_count": 3,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 3, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "wPYfBI0BZnyrIs2wNt-K",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "113.137.38.229",
                    "doc_count": 1,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "gs6VA40B043sXHpDLv2d",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "113.137.40.120",
                    "doc_count": 1,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.13",
                                    "_type": "_doc",
                                    "_id": "-UIVAo0BZnyrIs2wCjbW",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "113.141.176.103",
                    "doc_count": 1,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "xdOODo0BZnyrIs2w-hSv",
                                    "_score": 2.0,
                                    "_source": {"geoip": {"country_name": "China"}},
                                }
                            ],
                        }
                    },
                },
                {
                    "key": "117.33.177.31",
                    "doc_count": 1,
                    "country_tag": {
                        "hits": {
                            "total": {"value": 1, "relation": "eq"},
                            "max_score": 2.0,
                            "hits": [
                                {
                                    "_index": "access-www-xxxx-2024.01.15",
                                    "_type": "_doc",
                                    "_id": "z-ENDY0BZnyrIs2wdFwT",
                                    "_score": 2.0,
                                    "_source": {
                                        "geoip": {
                                            "country_name": "China",
                                            "region_name": "Shaanxi",
                                        }
                                    },
                                }
                            ],
                        }
                    },
                },
            ],
        },
        "day": {
            "buckets": [
                {"key_as_string": "2024-01-12", "key": 1705017600000, "doc_count": 168},
                {"key_as_string": "2024-01-13", "key": 1705104000000, "doc_count": 173},
                {"key_as_string": "2024-01-14", "key": 1705190400000, "doc_count": 172},
                {"key_as_string": "2024-01-15", "key": 1705276800000, "doc_count": 170},
                {"key_as_string": "2024-01-16", "key": 1705363200000, "doc_count": 168},
                {"key_as_string": "2024-01-17", "key": 1705449600000, "doc_count": 168},
                {"key_as_string": "2024-01-18", "key": 1705536000000, "doc_count": 21},
            ]
        },
    },
]


class TestXlsx(unittest.TestCase):
    pass

    def test_format_cnt(self):
        # print(xlsx._format_path(data))
        pass

    def test_create_xlsx(self):
        xlsx.create_xlsx("yuzhua.xlsx", data)
        pass


if __name__ == "__main__":
    unittest.main()
