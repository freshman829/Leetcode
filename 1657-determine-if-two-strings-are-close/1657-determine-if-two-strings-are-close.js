/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
function closeStrings(word1, word2) {
  if (word1.length !== word2.length) {
    return false;
  }

  const freq1 = {};
  const freq2 = {};

  for (const char of word1) {
    freq1[char] = (freq1[char] || 0) + 1;
  }

  for (const char of word2) {
    freq2[char] = (freq2[char] || 0) + 1;
  }

  const freqCounts1 = Object.values(freq1).sort().join(',');
  const freqCounts2 = Object.values(freq2).sort().join(',');

  const chars1 = Object.keys(freq1).sort().join(',');
  const chars2 = Object.keys(freq2).sort().join(',');

  return freqCounts1 === freqCounts2 && chars1 === chars2;
}

function isEqual(obj1, obj2) {
  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) {
    return false;
  }

  for (const key of keys1) {
    if (obj1[key] !== obj2[key]) {
      return false;
    }
  }

  return true;
}