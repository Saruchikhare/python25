#4 How memory is managed in Python?

"""Object Creation: Memory is allocated when objects are created.
Garbage Collection: Python's garbage collector reclaims memory from objects that are no longer referenced.
Reference Counting: Objects have a reference count, and memory is deallocated when the count drops to zero.
Cyclic Garbage Collection: Python's garbage collector detects and breaks cyclic references to reclaim memory.
Memory Pool: Python maintains a memory pool for efficient allocation and deallocation of small objects.
Memory Fragmentation: Memory fragmentation may occur over time, but Python's memory manager performs 
                        compaction to reduce fragmentation.
Manual Memory Management: Developers can manually manage memory using techniques like caching, weak 
                        references, and memory profiling tools."""
