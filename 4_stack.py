# ============================================
# DSA #4: STACK (LIFO)
# Real World Use: Hospital Appointment System
# ============================================
# Problem: Appointment book karo aur undo kar sako
# Solution: Stack — Last In, First Out (LIFO)
# Time Complexity: Push O(1), Pop O(1)
# ============================================


class AppointmentStack:
    """
    Stack = Plates ki tarah
    Upar se daalo (push) — upar se hi uthao (pop)
    Last In = First Out (LIFO)
    """

    def __init__(self):
        self._stack = []   # Python list as stack

    def book(self, patient, doctor, date, time):
        """
        Appointment book karo — PUSH operation
        List ke end mein add karo — O(1)
        """
        appointment = {
            "patient": patient,
            "doctor":  doctor,
            "date":    date,
            "time":    time
        }
        self._stack.append(appointment)   # PUSH
        print(f"✅ Booked: {patient} with {doctor} on {date} at {time}")
        print(f"   Stack size: {len(self._stack)}")

    def undo(self):
        """
        Last appointment cancel karo — POP operation
        List ke end se remove karo — O(1)
        LIFO: jo LAST aaya wo PEHLE jaayega
        """
        if not self._stack:
            print("❌ Koi appointment nahi hai!")
            return None

        removed = self._stack.pop()   # POP — last wala niklo
        print(f"↩️  Undo: {removed['patient']} ka appointment cancel hua")
        print(f"   ({removed['doctor']} | {removed['date']} | {removed['time']})")
        print(f"   Stack size: {len(self._stack)}")
        return removed

    def peek(self):
        """
        Top of stack dekho — bina remove kiye — O(1)
        Agla undo kaunsa hoga
        """
        if not self._stack:
            print("Stack empty hai")
            return None
        top = self._stack[-1]   # last element = top of stack
        print(f"👀 Top (next to undo): {top['patient']} — {top['doctor']}")
        return top

    def view_all(self):
        """Sari appointments dekho"""
        if not self._stack:
            print("Koi appointment nahi")
            return

        print(f"\n📅 All Appointments (Bottom → Top):")
        for i, appt in enumerate(self._stack):
            marker = " ← TOP (undo this first)" if i == len(self._stack) - 1 else ""
            print(f"  [{i+1}] {appt['patient']:15} | {appt['doctor']:25} | {appt['date']} {appt['time']}{marker}")

    def is_empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)


# ============================================
# DEMO
# ============================================
if __name__ == "__main__":
    print("=" * 55)
    print("  APPOINTMENT SYSTEM — STACK")
    print("  DSA: Stack (LIFO — Last In, First Out)")
    print("=" * 55)

    system = AppointmentStack()

    # Appointments book karo
    print("\n--- Appointments Book Ho Rahi Hain ---")
    system.book("Ali Hassan",    "Dr. Ahmed (Cardiology)",   "2025-06-15", "09:00")
    system.book("Sara Malik",    "Dr. Sara (Neurology)",     "2025-06-15", "10:30")
    system.book("Umar Sheikh",   "Dr. Hassan (Orthopedics)", "2025-06-16", "14:00")
    system.book("Fatima Bibi",   "Dr. Zara (General)",       "2025-06-17", "11:00")

    system.view_all()

    # Peek karo — top kaun hai
    print("\n--- Top of Stack ---")
    system.peek()

    # Undo karo
    print("\n--- Undo Operations ---")
    system.undo()   # Fatima wali cancel
    system.undo()   # Umar wali cancel

    system.view_all()

    # Aur book karo
    print("\n--- Nai Appointment Book Karo ---")
    system.book("Ahmed Khan", "Dr. Ali (ENT)", "2025-06-18", "15:00")

    system.view_all()

    # Sab undo karo
    print("\n--- Sab Undo Karo ---")
    while not system.is_empty():
        system.undo()

    system.undo()   # empty par try karo

    print("\n--- Stack vs Queue Comparison ---")
    print("Stack (LIFO): Last In = First Out")
    print("  → Undo/Redo, Browser back button, Function call stack")
    print("Queue (FIFO): First In = First Out")
    print("  → Print queue, Ticket counter, BFS traversal")

    print("\n--- Big-O Complexity ---")
    print("Push (book):    O(1) — end mein add karo")
    print("Pop  (undo):    O(1) — end se remove karo")
    print("Peek (top):     O(1) — last element dekho")
    print("Size:           O(1)")
