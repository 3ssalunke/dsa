# ENCODE & DECODE
def encode(strs):
  sizes = []
  wordstr = ''

  for s in strs:
      sizes.append(len(s))
      wordstr += s

  res = ",".join(map(str, sizes))
  return res + "#" + wordstr

def decode(s):
  if not s:
    return []

  sizes = []
  res = []
  hashidx = 0

  for i in range(len(s)):
    if s[i] == "#":
      hashidx = i
      break

  sizes = map(lambda x: int(x), s[:hashidx].split(","))

  prev = hashidx + 1
  for wordlen in sizes:
    next = prev + wordlen
    res.append(s[prev:next])
    prev = next

  return res
  
  