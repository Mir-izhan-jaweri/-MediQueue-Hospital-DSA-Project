# ============================================
# DSA #1: PRIORITY QUEUE (heapq)
# Real World Use: Hospital Emergency Triage
# ============================================
# Problem: Jo patient sabse critical hai,
#          usse pehle treat karo — chahe baad mein aaya ho
# Solution: Priority Queue (Min-Heap)
# Time Complexity: Insert O(log n), Get Min O(1)
# ============================================

import heapq

# Emergency queue — list as min-heap
queue = []

def add_patient(severity, name, age, complaint):
    """
    Patient ko queue mein add karo.
    Severity 1 = most critical (Heart Attack)
    Severity 5 = least critical (Cold)
    heapq automatically sabse chhota upar rakhta hai
    """
    heapq.heappush(queue, (severity, name, age, complaint))
    print(f"✅ Added: {name} | Severity: {severity} | Complaint: {complaint}")

def treat_next():
    """
    Sabse critical patient ko treat karo.
    heappop = min element nikalta hai — O(log n)
    """
    if not queue:
        print("❌ Queue empty hai!")
        return None

    severity, name, age, complaint = heapq.heappop(queue)
    labels = {1: "CRITICAL", 2: "EMERGENCY", 3: "URGENT", 4: "SEMI-URGENT", 5: "NON-URGENT"}
    print(f"🏥 Treating: {name} | Age: {age} | {labels[severity]} | Complaint: {complaint}")
    return name

def view_queue():
    """Queue dekho bina remove kiye"""
    if not queue:
        print("Queue empty hai")
        return
    print("\n📋 Current Queue (sorted by severity):")
    sorted_q = sorted(queue)  # copy sorted karo
    for i, (sev, name, age, complaint) in enumerate(sorted_q, 1):
        print(f"  {i}. [{sev}] {name} (Age {age}) — {complaint}")

def peek_next():
    """Agla patient kaun hai — bina nikale"""
    if queue:
        sev, name, age, complaint = queue[0]
        print(f"👀 Next to treat: {name} (Severity {sev})")
    else:
        print("Queue empty")


# ============================================
# DEMO — Yeh chala ke dekho
# ============================================
if __name__ == "__main__":
    print("=" * 50)
    print("  HOSPITAL EMERGENCY TRIAGE SYSTEM")
    print("  DSA: Priority Queue (heapq)")
    print("=" * 50)

    # Patients alag alag time par aate hain
    # Lekin severity ke hisaab se treat honge
    print("\n--- Patients Register Ho Rahe Hain ---")
    add_patient(3, "Ali Hassan",    35, "High Fever")       # pehle aaya
    add_patient(1, "Sara Malik",    60, "Heart Attack")     # baad mein aaya — lekin CRITICAL
    add_patient(5, "Ahmed Khan",    25, "Common Cold")
    add_patient(2, "Fatima Bibi",   45, "Road Accident")
    add_patient(1, "Umar Sheikh",   70, "Stroke")           # doosra critical patient

    view_queue()
    peek_next()

    print("\n--- Patients Treat Ho Rahe Hain ---")
    treat_next()   # Sara Malik (Severity 1) — Heart Attack
    treat_next()   # Umar Sheikh (Severity 1) — Stroke
    treat_next()   # Fatima Bibi (Severity 2) — Accident

    view_queue()

    print("\n--- Big-O Complexity ---")
    print("heappush (add):   O(log n)")
    print("heappop  (treat): O(log n)")
    print("queue[0] (peek):  O(1)    ← sabse fast!")
