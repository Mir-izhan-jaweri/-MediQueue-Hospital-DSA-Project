# ============================================
# DSA #2: BINARY SEARCH TREE (BST)
# Real World Use: Hospital Patient Records
# ============================================
# Problem: Lakhs patients mein se ek dhundna
# Solution: BST — har baar half records skip
# Time Complexity: O(log n) average
# ============================================

class Node:
    """BST ka ek node — patient ki info"""
    def __init__(self, patient_id, name, disease):
        self.patient_id = patient_id   # BST key
        self.name       = name
        self.disease    = disease
        self.left       = None         # chhote ID wale
        self.right      = None         # bade ID wale


class PatientBST:
    """
    Binary Search Tree for Patient Records
    Rule: Left child < Parent < Right child
    """

    def __init__(self):
        self.root = None

    def insert(self, patient_id, name, disease):
        """
        Naya patient insert karo.
        Har step par tree half hoti hai — O(log n)
        """
        self.root = self._insert(self.root, patient_id, name, disease)
        print(f"✅ Inserted: ID={patient_id} | {name} | {disease}")

    def _insert(self, node, pid, name, disease):
        # Base case: jagah mili — node banao
        if node is None:
            return Node(pid, name, disease)

        if pid < node.patient_id:
            node.left = self._insert(node.left, pid, name, disease)   # left side jao
        elif pid > node.patient_id:
            node.right = self._insert(node.right, pid, name, disease) # right side jao
        else:
            print(f"⚠️  ID {pid} already exists!")

        return node

    def search(self, patient_id):
        """
        Patient dhundho ID se.
        Har baar half tree ignore hoti hai — O(log n)
        """
        print(f"\n🔍 Searching for ID: {patient_id}...")
        steps = 0
        node = self.root

        while node:
            steps += 1
            print(f"   Step {steps}: Checking ID={node.patient_id}...", end=" ")

            if patient_id == node.patient_id:
                print("✅ Found!")
                print(f"   Patient: {node.name} | Disease: {node.disease}")
                print(f"   Total steps: {steps}")
                return node
            elif patient_id < node.patient_id:
                print(f"Go LEFT (target {patient_id} < {node.patient_id})")
                node = node.left
            else:
                print(f"Go RIGHT (target {patient_id} > {node.patient_id})")
                node = node.right

        print(f"❌ Patient ID {patient_id} nahi mila! Steps: {steps}")
        return None

    def inorder(self):
        """
        Inorder traversal = sorted order mein patients
        Left → Root → Right — O(n)
        """
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.patient_id, node.name, node.disease))
            self._inorder(node.right, result)

    def display_tree(self, node=None, level=0, prefix="Root: "):
        """Tree ko visually print karo"""
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + f"[{node.patient_id}] {node.name}")
            if node.left or node.right:
                if node.left:
                    self.display_tree(node.left, level + 1, "L── ")
                if node.right:
                    self.display_tree(node.right, level + 1, "R── ")


# ============================================
# DEMO
# ============================================
if __name__ == "__main__":
    print("=" * 50)
    print("  HOSPITAL PATIENT RECORDS — BST")
    print("  DSA: Binary Search Tree")
    print("=" * 50)

    bst = PatientBST()

    print("\n--- Patient Records Insert ---")
    bst.insert(1042, "Ali Hassan",    "Diabetes")
    bst.insert(756,  "Sara Malik",    "Fracture")
    bst.insert(1500, "Ahmed Khan",    "Fever")
    bst.insert(500,  "Zara Ali",      "Hypertension")
    bst.insert(900,  "Umar Sheikh",   "Asthma")
    bst.insert(1200, "Fatima Bibi",   "Arthritis")

    print("\n--- BST Structure ---")
    bst.display_tree()

    print("\n--- Patients Sorted by ID (Inorder) ---")
    for pid, name, disease in bst.inorder():
        print(f"  ID {pid}: {name} — {disease}")

    print("\n--- Search Demo ---")
    bst.search(900)    # milega
    bst.search(1200)   # milega
    bst.search(9999)   # nahi milega

    print("\n--- Big-O Complexity ---")
    print("Insert:  O(log n) average, O(n) worst case (skewed tree)")
    print("Search:  O(log n) average")
    print("Inorder: O(n)")
    print("\nFayda: 1,000,000 patients mein sirf ~20 steps mein dhundh sakte hain!")
