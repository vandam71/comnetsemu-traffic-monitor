import redis
import pymongo
import json

def main():
    # Connect to Redis
    redis_client = redis.StrictRedis(host='172.18.0.10', port=6379, db=0)
    
    # Connect to MongoDB
    mongo_client = pymongo.MongoClient("mongodb://172.18.0.11:27017/")
    db = mongo_client["traffic_monitor"]
    flow_stats_collection = db["flow_stats"]
    port_stats_collection = db["port_stats"]
    
    while True:
        # Process flow stats
        flow_stats_data = redis_client.lpop('flow_stats')
        if flow_stats_data:
            flow_stats = json.loads(flow_stats_data)
            flow_stats_collection.insert_one(flow_stats)
        
        # Process port stats
        port_stats_data = redis_client.lpop('port_stats')
        if port_stats_data:
            port_stats = json.loads(port_stats_data)
            port_stats_collection.insert_one(port_stats)

if __name__ == "__main__":
    main()
