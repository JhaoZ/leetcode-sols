#include <vector>
#include <deque>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <cstdint>

class Router {
public:
    struct Packet {
        int source;
        int destination;
        int timestamp;
    };

    explicit Router(int memoryLimit)
        : memlimit(memoryLimit), pointer(0), size(0) {}

    // ────────── addPacket ──────────
    bool addPacket(int source, int destination, int timestamp) {
        // create a new time bucket if needed
        if (timestamps.empty() || timestamps.back() != timestamp)
            timestamps.push_back(timestamp);

        /* 1) duplicate check – O(1)
              key = (src<<32)|dest (timestamp is fixed for the bucket)   */
        auto& dup = dupKey[timestamp];                      // one hash lookup
        std::uint64_t key = (static_cast<std::uint64_t>(source) << 32) |
                             static_cast<std::uint32_t>(destination);
        if (!dup.insert(key).second) return false;          // already present

        /* 2) store the packet                                                    */
        levels[timestamp].push_back({source, destination, timestamp});
        ++size;

        /* 3) update per-destination index – timestamps are ALWAYS appended
              in non-decreasing order, so each deque stays sorted.                */
        destTimes[destination].push_back(timestamp);

        /* 4) respect memory limit                                                */
        if (size > memlimit) evictOldest();
        return true;
    }

    // ────────── forwardPacket ──────────
    std::vector<int> forwardPacket() {
        if (!advancePointer()) return {};

        auto& bucket = levels[timestamps[pointer]];
        Packet pkt   = bucket.front();
        bucket.pop_front();
        removeFromIndices(pkt);                            // maintain aux-structures
        return {pkt.source, pkt.destination, pkt.timestamp};
    }

    // ────────── getCount – O(log n) ──────────
    int getCount(int destination, int startTime, int endTime) {
        auto it = destTimes.find(destination);
        if (it == destTimes.end()) return 0;

        const auto& dq = it->second;                       // sorted deque<int>
        auto lo = std::lower_bound(dq.begin(), dq.end(), startTime);
        auto hi = std::upper_bound(lo,        dq.end(),   endTime);
        return static_cast<int>(hi - lo);
    }

private:
    /* ────────── helpers ────────── */

    // advance pointer to first non-empty bucket
    bool advancePointer() {
        while (pointer < timestamps.size() &&
               levels[timestamps[pointer]].empty()) {
            if (pointer == timestamps.size() - 1) return false;
            ++pointer;
        }
        return pointer < timestamps.size();
    }

    // evict one packet (the oldest in the current pointer bucket)
    void evictOldest() {
        if (!advancePointer()) return;                      // nothing to evict
        auto& bucket = levels[timestamps[pointer]];
        Packet victim = bucket.front();
        bucket.pop_front();
        removeFromIndices(victim);
    }

    // remove packet from duplicate-set & per-destination index
    void removeFromIndices(const Packet& pkt) {
        --size;

        // 1) duplicate-set
        std::uint64_t key = (static_cast<std::uint64_t>(pkt.source) << 32) |
                             static_cast<std::uint32_t>(pkt.destination);
        auto& dup = dupKey[pkt.timestamp];
        dup.erase(key);
        if (dup.empty()) dupKey.erase(pkt.timestamp);

        // 2) destination-time index (front is always the oldest)
        auto& dq = destTimes[pkt.destination];
        dq.pop_front();
        if (dq.empty()) destTimes.erase(pkt.destination);
    }

    /* ────────── data members ────────── */
    std::unordered_map<int, std::deque<Packet>>       levels;   // ts → queue
    std::unordered_map<int, std::unordered_set<std::uint64_t>> dupKey;   // ts → {src|dest}
    std::unordered_map<int, std::deque<int>>          destTimes; // dest → sorted ts

    std::vector<int>      timestamps;   // ordered list of unique time-stamps
    std::size_t           pointer;      // index into timestamps (oldest bucket)
    const int             memlimit;     // maximum #packets kept
    int                   size;         // current #packets
};
