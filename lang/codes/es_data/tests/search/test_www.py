import asyncio
import unittest
from app.search.www import Site


class AsyncTestCase(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    def tearDown(self):
        self.loop.close()


class TestSite(AsyncTestCase):
    def setUp(self) -> None:
        self.sql = """
        SELECT server_name, count(*)
        FROM k8s-nginx
        WHERE "@timestamp" >= '2023-08-01'
        AND "@timestamp" <= '2023-08-19'
        GROUP BY "server_name"
        """

    async def test_execute_query(self):
        s = Site("","")
        result = await s.execute_query(self.sql)
        print("xxxxxxxx ", result)


if __name__ == "__main__":
    unittest.main()