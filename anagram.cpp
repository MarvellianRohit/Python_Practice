#include <iostream>
#include <string>
#include <vector>

bool isAnagram(std::string s, std::string t) {
  // Step 1: If lengths are different, they cant be anagrams
  if (s.length() != t.length()) {
    return false;
  }

  // Step 2:  Create our "buckets"
  // Since there are 26 letters, an array of size 26 initialized to 0.
  int count[26] = {0};

  // Step 3: Fill and Drain the Buckets
  for (int i = 0; i < s.length(); i++) {
    // s[i] - 'a' converts a char like 'b' into an index (1)
    count[s[i] - 'a']++;
    count[t[i] - 'a']--;
  }

  // Step 4: Check if all buckets are zero
  for (int i = 0; i < 26; i++) {
    if (count[i] != 0) {
      return false;
    }
  }

  return true;
}

int main() {
  std::string s1 = "anagram", t1 = "nagaram";
  std::cout << (isAnagram(s1, t1) ? "True" : "False") << std::endl;
  return 0;
}