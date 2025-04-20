from pymongo import MongoClient
import matplotlib.pyplot as plt 

mongo_client = MongoClient("mongodb://mongo:27017/")
db = mongo_client["linq_db"]
collection = db["linq_collection"]

docs = list(collection.find())
if not docs:
    print("No data found in collection.")
    exit()

rank_kdr = {}
rank_count = {}

for doc in docs:
    rank = doc.get('rank')
    kdr = doc.get('kdr', 0)

    if rank and isinstance(kdr, (int, float)):
        rank_kdr[rank] = rank_kdr.get(rank, 0) + kdr
        rank_count[rank] = rank_count.get(rank, 0) + 1

avg_kdr_by_rank = {
    rank: round(rank_kdr[rank] / rank_count[rank], 2)
    for rank in rank_kdr
    if rank_count[rank] > 0
}

if not avg_kdr_by_rank:
    print("Data was loaded, but average KDRs couldn't be calculated.")
    exit()

sorted_ranks = sorted(avg_kdr_by_rank.keys())
avg_kdrs = [avg_kdr_by_rank[rank] for rank in sorted_ranks]

plt.figure(figsize=(8, 5))
bars = plt.bar(sorted_ranks, avg_kdrs, color='skyblue', edgecolor='black')
plt.title("Average KDR by Rank")
plt.xlabel("Player Rank")
plt.ylabel("Average KDR")
plt.ylim(0, max(avg_kdrs) + 1)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.05, f"{yval:.2f}", ha='center')

plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()