# Tier 0 — The 50-Exercise Ladder

**For:** Xasanboy · **Covers:** all of Tier 0 (Python foundations) · **Replaces:** grinding all 456

These are not the 456. This is a curated climb across *every* Tier-0 skill — control flow → strings → data structures → **file I/O** (the half the 456 never touch) → functions & errors → generators → OOP → decorators & context managers → two capstones. Solve them roughly in order; the early ones are doable today, the late ones you grow into as you reach those rungs. Don't brute-force #45 this week — that's its own gate-skip.

---

## How to use this

- **Naming:** your solution for exercise N is a function named `tier_N`. Where a harder second version is offered, name it `tier_N_complicated`. (The review tool finds your work by these names — keep the convention exact.)
- **One file or many:** your call. `tier_01.py … tier_50.py`, or grouped by block. Just keep `tier_N` discoverable.
- **You write everything.** These are specs and test cases, not stubs. I give you the contract (what goes in, what comes out, an example) and the *name of the muscle* being trained. The implementation — including the function signature — is yours. That's the Iron Rule, and it's the whole point.
- **Type hints become mandatory from Block E (#28) onward.** Annotate every parameter and return. Earlier blocks: annotate if you want the reps, but designing the signature yourself is part of the exercise.
- **Standing stretch (Block D onward):** for any exercise, write one `pytest` test that proves it holds on an edge case. Optional, but it's a Tier-0 bar and a free habit to build.

**Legend** — difficulty: ● easy · ●● medium · ●●● hard · **★** = genuine logic-stretcher (expect to be stuck; that's correct) · **⊕** = a `tier_N_complicated` version is offered · **→** = foreshadows a real roadmap project.

**The hard constraint: bare Python only.** Standard library, nothing else. No NumPy, no pandas, no scikit-learn — not because they're bad, but because they *hide the exact logic you're rebuilding*. You writing `mean()` by hand is the lesson; `df.mean()` erases it. Those libraries are Tier 1–3, and reaching for them now is the gate violation this whole roadmap exists to prevent. The scenarios are the real job; the tools stay basic on purpose.

---

## Block A — Control flow & numbers (1–6)
*The on-ramp. Re-warming logic. Doable today.*

> **Ground rules for every exercise below:**
> - Match the given signature exactly — name, parameters, return type. No `input()`, no `print()` inside the function, unless the exercise explicitly says it's interactive (only #6 does).
> - The function must **return** its answer. Printing is not returning.
> - When the contract below doesn't say what to do for a case — an empty list, for instance — that's deliberate, not a gap. Deciding what should happen there is part of the exercise.
> - One worked example is given per exercise, so you know your function is pointed the right way. It is not the full test suite. Finding what it doesn't cover is your job.

**1. Confidence bucketer** ● · loops, conditionals, counting
```
def tier_1(scores: list[float]) -> dict[str, int]:
```
- **Given:** a list of floats.
- **Must return:** a dict with exactly the keys `"low"`, `"mid"`, `"high"` — the count of scores that are `<0.4`, `<0.8`, and `>=0.8`, respectively.
- **Example:** `tier_1([0.91, 0.2, 0.55, 0.99])` → `{"low": 1, "mid": 1, "high": 2}`

**2. Summary stats, by hand** ●● · accumulation, comparison
```
def tier_2(numbers: list[float]) -> tuple[float, float, float]:
```
- **Given:** a list of numbers.
- **Must return:** `(minimum, maximum, mean)`, in that order — computed **without** `min()`, `max()`, or `sum()`. Use a loop; understand what those built-ins do for you.
- **Example:** `tier_2([3, 1, 2])` → `(1, 3, 2.0)`

```
def tier_2_complicated(numbers: list[float]) -> tuple[float, float, float, float]:
```
- **Given:** a list of numbers.
- **Must return:** `(minimum, maximum, mean, median)`. Built-ins are allowed now. For an even-length list, the median is the **average of the two middle values** (one number, not two) — sort first, then handle even vs. odd length.
- **Example:** `tier_2_complicated([1, 2, 3, 4])` → `(1, 4, 2.5, 2.5)`

**3. Longest streak** ●●● **★** · stateful iteration
```
def tier_3(values: list[float], threshold: float) -> int:
```
- **Given:** a list of daily values, and a threshold.
- **Must return:** the length of the longest run of *consecutive* values that stayed strictly above the threshold. `0` if no value ever exceeds it.
- **Example:** `tier_3([1, 5, 6, 2, 7, 8, 9, 1], 4)` → `3` (the run 7, 8, 9)
- *Trap: you need to track "current run" and "best run so far" separately, and reset at the right moment.*

**4. ID checksum validator** ●●● · indexing, modular arithmetic
```
def tier_4(number: str) -> bool:
```
- **Given:** a string of digits.
- **Must return:** `True` if it passes the Luhn check-digit rule, else `False`. The rule: starting from the rightmost digit, double every second digit; if doubling produces a two-digit number, sum its two digits; total every digit (doubled-and-reduced or not); valid iff that total is divisible by 10.
- **Example:** `tier_4("4561261212345467")` → `True`
- *Trap: "from the right" and the doubling-then-digit-sum step are where it breaks.*

**5. Human-readable units** ●● · integer division, modulo, formatting

Two separate functions — not one function with a mode switch:
```
def tier_5_bytes(n: int) -> str:
```
- **Given:** a byte count.
- **Must return:** a string using 1024-based steps (B, KB, MB, GB, TB).
- **Example:** `tier_5_bytes(2400000)` → `"2.29 MB"`

```
def tier_5_seconds(n: int) -> str:
```
- **Given:** a count of seconds.
- **Must return:** a duration string with zero-valued components dropped entirely.
- **Example:** `tier_5_seconds(90)` → `"1m 30s"` — not `"0h 1m 30s"`, not a decimal-minutes string.

**6. Clean averaging loop** ●● · input loop, validation, sentinel

This one really is interactive — but split the validation out from the loop, so the part that actually had last time's bug is testable on its own:
```
def tier_6_parse(raw: str) -> float | None:
```
- **Given:** one already-stripped input string (never `"q"`/`"exit"`/`"quit"` — the loop below handles those separately).
- **Must return:** the parsed number as a `float` if `raw` is a valid real number (negatives allowed), else `None`.
- **Example:** `tier_6_parse("3.14")` → `3.14` · `tier_6_parse("-")` → `None`

```
def tier_6() -> float | None:
```
- **Given:** nothing — it gets numbers by calling `input()` in a loop, validating each with `tier_6_parse`, until `q`/`exit`/`quit`.
- **Must:** print the mean **and** return it. (`input()`/`print()` are expected and fine in this one function only.)

`tier_6_complicated`: same shape, two more functions —
```
def tier_6_complicated_parse(raw: str) -> float | None:
def tier_6_complicated() -> float | None:
```
- `tier_6_complicated_parse` accepts everything `tier_6_parse` does, **plus** comma as a decimal separator (`"3,14"` → `3.14`), while still rejecting a lone `-`, `.`, or `,`.
- **Example:** `tier_6_complicated_parse("3,14")` → `3.14`

---

## Block B — Strings & text (7–13)
*The rawest form of ML data work. This is where NLP lives.*

> **Ground rules** (same as Block A): match the given signature exactly — name, parameters, return type. No `input()`/`print()` inside any of these; every one is a plain function this time, no exceptions. The function must **return** its answer. Unstated cases (empty string, a key missing from a dict, malformed input) are deliberately left to you. One example is given per exercise to point you the right way — it is not the full test suite.

**7. Tokenizer** ●● · string methods, iteration
```
def tier_7(text: str) -> list[str]:
```
- **Given:** a string.
- **Must return:** the words in `text`, lowercased, with punctuation stripped, in original order (duplicates kept).
- **Example:** `tier_7("Hello, WORLD! Hello.")` → `["hello", "world", "hello"]`

**8. Word frequency (in memory)** ●● · dict accumulation
```
def tier_8(text: str) -> dict[str, int]:
```
- **Given:** a string.
- **Must return:** a dict mapping each word (lowercased, punctuation stripped) to how many times it appears.
- **Example:** `tier_8("the cat the dog")` → `{"the": 2, "cat": 1, "dog": 1}`

```
def tier_8_complicated(text: str, n: int) -> list[tuple[str, int]]:
```
- **Given:** a string, and how many top words to return.
- **Must return:** a list of `(word, count)` pairs — the `n` most frequent words, sorted by count descending; ties broken alphabetically by word. (A `dict` can't express this: dict equality doesn't care about order, so it can't check that you got the ranking right — that's why this one returns a list.)
- **Example:** `tier_8_complicated("the cat the dog the bird cat", 3)` → `[("the", 3), ("cat", 2), ("bird", 1)]` — `"bird"` beats `"dog"` for third place because they're tied at 1 and `"bird"` comes first alphabetically.

**9. Latin ↔ Cyrillic normalizer** ●●● **★** · dict lookup, string building
```
def tier_9(text: str) -> str:
```
- **Given:** a string built only from the standard Uzbek Latin single letters (`a, b, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, x, y, z`) plus the four digraphs `sh`, `ch`, `o'`, `g'` — assume clean, native-vocabulary words only. No loanword spellings, no apostrophe-as-glottal-stop, no case where `s` and `h` are meant separately. That real-world mess is exactly why project #5 (`uztext`) is a 12-hour library later, not a 20-minute exercise now — this rung is scoped to the clean case on purpose.
- **Must return:** the Cyrillic transliteration.
- **Example:** `tier_9("shahar")` → `"шаҳар"`
- *Trap: `sh` is one Cyrillic letter, but a naive scanner sees `s` then `h` separately. Multi-character sequences must be matched before single ones. This is the actual hard part of your real `uztext` package.*

**10. Hamming distance** ●● · parallel iteration
```
def tier_10(a: str, b: str) -> int:
```
- **Given:** two strings of equal length.
- **Must return:** the count of positions where they differ.
- **Example:** `tier_10("karol", "kapol")` → `1`

```
def tier_10_complicated(a: str, b: str) -> int:
```
- **Given:** two strings, any lengths (not necessarily equal).
- **Must return:** the full Levenshtein edit distance — the minimum number of single-character insertions, deletions, and substitutions to turn `a` into `b`.
- **Example:** `tier_10_complicated("kitten", "sitting")` → `3` (a well-known textbook case — worth checking your answer against a source you trust before deciding it's right)
- Optional. Real dynamic programming, and the hardest thing in this block — starred for a reason.

**11. Log-level counter** ●● · string splitting, dict counting
```
def tier_11(log_lines: list[str]) -> dict[str, int]:
```
- **Given:** a list of log line strings, each shaped like `"2026-06-26 14:03:12 ERROR auth: bad token"` — a timestamp, then a level, then a colon-separated message.
- **Must return:** a dict mapping each level that actually appears to its count. (A level with zero occurrences shouldn't show up at all — see the example.)
- **Example:** `tier_11(["2026-06-26 14:03:12 ERROR auth: bad token", "2026-06-26 14:03:15 INFO auth: login ok", "2026-06-26 14:03:16 ERROR auth: bad token"])` → `{"ERROR": 2, "INFO": 1}` — no `"WARN"` key, since none appeared.

**12. CSV line parser, by hand** ●●● **★** · char-by-char state machine
```
def tier_12(line: str) -> list[str]:
```
- **Given:** one line of comma-separated text, which may contain a quoted field with a comma inside it.
- **Must return:** the list of fields, in order, with the surrounding quotes of any quoted field removed.
- **Must not use:** the `csv` module.
- **Example:** `tier_12('Tashkent,"Yunusobod, 5",2026')` → `["Tashkent", "Yunusobod, 5", "2026"]` — three fields, not four.
- *Trap: you need a flag for "am I currently inside quotes?" This is exactly what `pandas.read_csv` does for you under the hood — build it once so you know.*

**13. Template renderer** ●● · string scanning, dict lookup
```
def tier_13(template: str, values: dict[str, object]) -> str:
```
- **Given:** a template string containing `{key}` placeholders, and a dict of values.
- **Must return:** the template with each `{key}` replaced by its value (converted to text) — **without** using `.format()` or an f-string to do the substitution. Scan and build the result yourself.
- **Example:** `tier_13("Hello {name}, you have {count} messages", {"name": "Xas", "count": 3})` → `"Hello Xas, you have 3 messages"`

---


## Block C — Lists, comprehensions & data structures (14–21)
*Choosing the right structure by instinct.*

> **Ground rules** (same as Blocks A and B): match the given signature exactly. No `input()`/`print()` — every one of these is a plain function. The function must **return** its answer. Unstated cases are deliberately left to you. One example per exercise points you the right way; it is not the full test suite.
>
> **New standing rule for this block:** don't mutate the input. Every function here takes a list or dict and must leave it exactly as it found it — build and return a new one. Silently modifying a caller's data is one of the nastier bug classes in data code, and this is the block where the temptation starts.

**14. Order-preserving dedup** ●● · set + list
```
def tier_14(items: list) -> list:
```
- **Given:** a list, possibly with duplicates.
- **Must return:** a new list keeping only the **first** occurrence of each value, in original order.
- **Must do it in one pass** — a set for "have I seen this," a list for output. Not a nested loop scanning back over the output each time.
- **Example:** `tier_14([3, 1, 3, 2, 1])` → `[3, 1, 2]`

```
def tier_14_complicated(records: list[dict], key: str) -> list[dict]:
```
- **Given:** a list of dicts, and the name of the field to dedup on.
- **Must return:** a new list keeping the **first** record for each distinct value of `records[i][key]`, in original order.
- **Example:** `tier_14_complicated([{"id": 1, "n": "a"}, {"id": 2, "n": "b"}, {"id": 1, "n": "c"}], "id")` → `[{"id": 1, "n": "a"}, {"id": 2, "n": "b"}]` — the third record is dropped; the one kept is the *first* `id=1`, so `"n"` is `"a"`, not `"c"`.
- This is `drop_duplicates(subset=...)`.

**15. Group-by** ●● · dict-of-lists
```
def tier_15(pairs: list[tuple[str, float]]) -> dict[str, list[float]]:
```
- **Given:** a list of `(category, value)` pairs.
- **Must return:** a dict mapping each category to the list of its values, **in the order they appeared**.
- **Example:** `tier_15([("a", 1), ("b", 2), ("a", 3)])` → `{"a": [1, 3], "b": [2]}`

```
def tier_15_complicated(pairs: list[tuple[str, float]]) -> dict[str, float]:
```
- **Given:** the same.
- **Must return:** a dict mapping each category to the **mean** of its values.
- **Example:** `tier_15_complicated([("a", 1), ("b", 2), ("a", 3)])` → `{"a": 2.0, "b": 2.0}`
- This is `groupby().mean()`.

**16. Flatten & filter** ●● · comprehension fluency
```
def tier_16(nested: list[list[int]]) -> list[int]:
```
- **Given:** a list of lists of ints.
- **Must return:** one flat list containing only the **even** numbers, in original order.
- **Must be written as a single comprehension** — that's the skill being drilled. (A loop version would pass the tests and miss the point; see the note in Block B about solving the right exercise.)
- **Example:** `tier_16([[1, 2], [3, 4], [5]])` → `[2, 4]`

**17. Transpose** ●● · nested iteration
```
def tier_17(rows: list[list]) -> list[list]:
```
- **Given:** a list of rows, all the same length (a rectangular grid).
- **Must return:** the list of columns.
- **Example:** `tier_17([[1, 2, 3], [4, 5, 6]])` → `[[1, 4], [2, 5], [3, 6]]`

```
def tier_17_complicated(rows: list[list]) -> list[list]:
```
- **Given:** the same. **Must return:** the same result — but written with `zip(*rows)` instead of index arithmetic.
- The point is to write it both ways and understand why they're equivalent. Note `zip` yields tuples, and the contract says lists.

**18. Min-max normalization** ●● · two-pass scaling
```
def tier_18(values: list[float]) -> list[float]:
```
- **Given:** a list of numbers.
- **Must return:** a new list scaled to the range [0, 1] by `(x - min) / (max - min)`.
- **Example:** `tier_18([10, 20, 30])` → `[0.0, 0.5, 1.0]`
- *Trap: what if every value is identical? Then `max - min` is `0`, and the formula divides by zero. The spec deliberately doesn't say what to do — decide, and be able to say why.*

**19. One-hot encoder** ●●● · set vocab, index mapping
```
def tier_19(labels: list[str]) -> list[list[int]]:
```
- **Given:** a list of category labels.
- **Must return:** one vector per input label, in input order. The vocabulary is the **sorted** unique labels; each vector is all `0`s with a single `1` at that label's index in the vocabulary.
- **Example:** `tier_19(["cat", "dog", "cat"])` → `[[1, 0], [0, 1], [1, 0]]` — vocabulary is `["cat", "dog"]`, so `cat` puts its `1` at index 0.
- Sorting the vocabulary is what makes this reproducible; without it the same data could encode differently between runs.

**20. Sliding-window batches** ●● · slicing
```
def tier_20(items: list, k: int) -> list[list]:
```
- **Given:** a list and a batch size `k`.
- **Must return:** consecutive **non-overlapping** chunks of size `k`; the final chunk may be shorter.
- **Example:** `tier_20([1, 2, 3, 4, 5], 2)` → `[[1, 2], [3, 4], [5]]`
- *You'll rewrite this as a generator in #36 — keep your solution.*

**21. Sparse dot product** ●●● **★** · dict iteration, an efficiency insight
```
def tier_21(a: dict[int, float], b: dict[int, float]) -> float:
```
- **Given:** two sparse vectors as dicts mapping index → value. An index absent from a dict means its value there is `0`.
- **Must return:** their dot product — the sum of `a[i] * b[i]` over every index `i` present in **both**.
- **Must iterate only the shorter dict**, looking up the other. Understand why that matters when one vector has 10 entries and the other has 100,000.
- **Example:** `tier_21({0: 2, 3: 1}, {3: 4, 5: 9})` → `4` — only index `3` appears in both: `1 × 4`. Index `0` and index `5` contribute nothing, because the other vector is `0` there.

```
def tier_21_complicated(a: dict[int, float], b: dict[int, float]) -> float:
```
- **Given:** the same two sparse vectors.
- **Must return:** their cosine similarity — the dot product divided by the product of their magnitudes, where a vector's magnitude is the square root of the sum of its squared values.
- **Example:** `tier_21_complicated({0: 3, 1: 4}, {0: 3, 1: 4})` → `1.0` — a vector compared to itself is maximally similar, whatever its magnitude. That's a useful self-check: if your function doesn't return `1.0` here, it's wrong, and you don't need a second test to know it.
- *Trap: what if a vector is empty, or all zeros? Its magnitude is `0`, and you're dividing by it again.*
- This is the math under every semantic search you'll ever build.

---


## Block D — File I/O (22–27)
*The half of item 1 the 456 never touched. This is the closer.*

> **Data:** you need real files to read. Use what's around — your own `.py` files, a free book from Project Gutenberg (`gutenberg.org`), a log from your VPS, or a small open dataset from `data.egov.uz` (which doubles as recon for roadmap project #4). Messy real data beats a clean fixture.

**22. File `wc`** ● · open/read, the `with` statement
Read a text file and report its line count, word count, and character count. The on-ramp to file I/O.

**23. Word frequency, from a file** ●● · full read→process→write round trip · ⊕ · **← this is the item-1 diagnostic**
Read a text file, compute word frequencies (reuse #8's logic), and **write** the top-N results to an output file, one `word: count` per line. This is the exercise that actually closes Tier-0 item 1 — file I/O + the dict work, end to end.
`tier_23_complicated`: take input/output filenames and N as arguments; handle the input file not existing (ties to Block E).

**24. Log filter** ●● · read-process-write pipeline
Read a log file, write only the `ERROR` lines to a new file, and print how many you wrote. ETL in its simplest form.

**25. Merge files** ●● · iterating files, accumulation
Given several filenames, concatenate them into one output file. Combining data shards.
`tier_25_complicated`: dedup lines across all files while merging.

**26. Real CSV summary** ●●● · `csv` module, type conversion, aggregation · ⊕
Now you **may** use the `csv` module (contrast #12). Read a CSV with a header, then compute something real: the mean of one numeric column and the counts within one categorical column.
`tier_26_complicated`: skip malformed rows (wrong field count, non-numeric where a number's expected) without crashing — collect how many you skipped.

**27. JSON config round-trip** ●● · `json` load/dump · →every repo's config
Read a JSON config file, change one value, write it back out preserving the rest. Managing experiment settings.

---

## Block E — Functions, scope & error handling (28–35)
*Type hints are now mandatory. Annotate everything.*

**28. Refactor into pure functions** ●● · decomposition, tuple return
Take a small task (e.g. #2's stats) and split it into single-responsibility functions, returning multiple values as a tuple and unpacking at the call site. (Your `ex_1` was one big function — this is the fix.)

**29. Flexible aggregator** ●● · `*args`, `**kwargs`, defaults
Write `tier_29(*numbers, method="mean")` accepting any count of numbers and an optional method (`"mean"`/`"min"`/`"max"`). Flexible APIs start here.
`tier_29(1, 2, 3, method="max") → 3`

**30. Your own map & filter** ●●● · functions as arguments
Write a function that takes a list and a function, and returns a new list with that function applied to each element (your own `map`). Then one taking a list and a predicate, returning only matching elements (your own `filter`). This is the engine under `.apply()`.

**31. Safe number parser** ●● · `try`/`except`, EAFP · ←the `is_valid` payoff
Write the clean, idiomatic answer to your old `is_valid`: a function taking a string, returning the parsed number, or a default you pass in (or raising) when conversion fails — using `try`/`except`, not character-by-character checking. I told you the clean answer is ~3 lines. Write those 3 lines.

**32. Custom exception** ●● · `raise`, custom exception class
Define a `ValidationError`. Write a function that raises it (with a useful message) when input breaks a rule, and a caller that catches it and reports cleanly. Production input-validation.

**33. Retry wrapper** ●●● · `try`/`except` in a loop · →every LLM/API call
Write a function that calls another function and, if it raises, retries up to `n` times before giving up (re-raising the last error). Simulate flakiness with a function that fails randomly. Every network/LLM call you'll ever make needs this.
*(You'll rebuild this as a decorator in #45.)*

**34. Batch with partial failure** ●●● · `try`/`except` inside iteration · →agentic doc processor (#12)
Process a list of items where some raise. Collect successes and failures **separately** and return both — one bad item must not kill the batch. This is processing 1,000 documents where 12 are corrupt.

**35. Memoize by hand** ●●● **★** · closures, enclosing scope
Write a function that returns another function which caches its results in an enclosing-scope dict, so repeated calls with the same argument skip the (simulated expensive) work.
*Trap: scope is where this bites — where does the cache live, and does it survive between calls? (It should.)*

---

## Block F — Generators & laziness (36–40)
*Streaming data too big to hold in memory.*

**36. List → generator** ●● · `yield`, lazy evaluation
Rewrite #20 (sliding-window batches) as a generator using `yield`. Then explain, in a comment, why this version uses less memory.

**37. Lazy file reader** ●●● · `yield` + file iteration · →why DuckDB exists
A generator that yields parsed records from a file one at a time, never loading the whole file. This is how you process a 10 GB log on an 8 GB laptop.

**38. Infinite sequence + `take`** ●●● · infinite generators
Write a generator producing an unbounded sequence (e.g. exponential backoff: 1, 2, 4, 8, …), plus a `take(gen, n)` function returning its first `n` values as a list. Backoff schedules, id generation.

**39. Generator pipeline** ●●● **★** · generator composition
Chain three generators — read → clean → filter — so data flows through lazily, one item at a time, never materializing the full list between stages. This is a streaming ETL pipeline, and composing laziness is a real mental leap.

**40. Running-stats generator** ●●● · stateful generator
A generator fed a stream of numbers that yields the running mean *after each one*. (Callback to #1, now lazy and incremental — an online algorithm.)
`feed 2, 4, 6 → yields 2.0, 3.0, 4.0`

---

## Block G — OOP (41–43)
*When state that persists across calls makes a class beat a function.*

**41. `RunningStats` class** ●● · `__init__`, methods, `@property`
Encapsulate the streaming-stats idea as a class: `.add(x)` updates internal state; `.mean`, `.count`, `.min`, `.max` are available at any time (make at least one a `@property`). The natural "this is why a class beats a function" lesson — the state lives in the object.

**42. `Vocabulary` class** ●●● · class state, two dicts in sync · →news classifier (#9), embeddings (#14)
Build the token↔id object every NLP codebase has: `.add(token)` returns its integer id (new or existing), `.encode(tokens)` → list of ids, `.decode(ids)` → list of tokens. Keep a `token→id` and an `id→token` dict consistent. This is real, and it's yours forever.
`v.add("cat")→0, v.add("dog")→1, v.add("cat")→0; v.encode(["dog","cat"])→[1,0]`

**43. `Dataset` / `DataLoader`-lite** ●●● · dunder methods · →PyTorch (Tier 4)
A class wrapping a list that supports `len(ds)` (`__len__`), `ds[i]` (`__getitem__`), and iteration in batches (`__iter__` yielding lists of size `batch_size`). This is literally PyTorch's `Dataset`/`DataLoader` interface, in pure Python. You're building the thing you'll meet again in Tier 4.

---

## Block H — Decorators & context managers (44–48)

**44. Timing decorator** ●● · decorator syntax, `*args`/`**kwargs` passthrough · →cost/latency (#13)
A decorator that measures how long the wrapped function takes and reports it, while passing arguments and the return value through untouched. (Look up `functools.wraps` and use it.)

**45. Retry decorator** ●●● **★** · parametrized decorator · →every LLM call
#33 as a decorator you apply like `@retry(times=3)`. The parameter means three layers of nesting — this is the decorator pattern that trips everyone, and it's worth owning.

**46. Timing context manager** ●●● · `__enter__`/`__exit__` · →cost/latency (#13)
A `with timer():` block that prints the elapsed time when it exits. Build it as a class with the context-manager protocol (then, optionally, look at `contextlib`).

**47. Safe-resource context manager** ●●● · cleanup on exit, even on error
A context manager that acquires a resource (a file, or a simulated connection) and **guarantees** release on exit — even if the body raises. Production resource hygiene.

**48. Caching decorator** ●●● · decorator + closure cache
#35 (memoize) as a decorator. Combine the two patterns: the decorator wraps, the closure holds the cache. Caching expensive calls — embeddings, LLM responses.

---

## Block I — Capstones (49–50)
*Pull it all together. Slightly larger. Portfolio-shaped.*

**49. Word-frequency CLI tool** ●●● · file I/O + dicts + functions + errors, integrated · →CLI projects (#1, #3)
A small, real program: read a text file (filename as argument), tokenize, count, handle a missing file gracefully, and print or write the top-N words. Structured into typed, single-responsibility functions. This is the shape of your roadmap's first real project.

**50. In-memory retriever — "RAG" with no libraries** ●●● **★** · everything composed · ⊕ · →flagship NormaRAG (#11)
Given a list of short documents and a query string, score each document by word-overlap with the query (or reuse #21's cosine over word-count vectors), and return the top-k most relevant documents. This is the **core idea of retrieval** — the engine of your entire career wedge — in pure Python, before any vector database exists.
`tier_50_complicated`: weight rarer words more (term-frequency scoring) and measure whether ranking improves.

---

## Where this leaves Tier 0

These 50 exercise **every codeable Tier-0 skill**: control flow, data structures, file I/O, functions & scope, error handling, OOP, comprehensions, generators, decorators, context managers, and (from #28) type hints. What they *don't* cover — Git, GitHub, the Linux/CLI work, `uv`/`ruff`/`pre-commit` — isn't code-shaped; that's tooling, and it comes just before your first CLI project.

**#23 is the item-1 closer.** It's the file-I/O diagnostic, complete. And none of this replaces **CS50P Problem Set 0** — this set *feeds* it. Reps on the ladder, then the ladder.
