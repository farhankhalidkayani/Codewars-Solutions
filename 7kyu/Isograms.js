// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

// Example: (Input --> Output)

// "Dermatoglyphics" --> true
// "aba" --> false
// "moOse" --> false (ignore letter case)

function isIsogram(str) {
  let hashtable = new Map();
  for (let c of str) {
    if (hashtable.has(c.toLowerCase())) {
      return false;
    }

    hashtable.set(c.toLowerCase(), 1);
  }

  return true;
}
