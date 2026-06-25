# TODO (EduSmart) — Bug fix & performance improvement

- [x] Fix quiz feature mismatch (bug fix):
  - [x] Implement server-side filtering by `mode` (mcq/essay/all) and `level` (easy/medium/hard) when rendering + scoring.

- [x] Fix quiz attempt counter behavior:
  - [x] Ensure `attempts_{quiz_id}` increments only after valid POST submissions.

- [ ] Performance improvements:
  - [ ] Avoid re-loading `quiz.json` per request by loading it once at startup (in `models.py` already done, verify relative file path correctness).
  - [ ] Replace costly per-request list building in `quiz_index`/lesson routes where feasible (e.g., memoize grouped quizzes, cache subject list).

- [x] Correctness/UI:
  - [x] Ensure `templates/results.html` matches the data passed by `app.py` (`results`, `score`, `total`).

- [ ] Testing:
  - [ ] Run Flask and verify:
    - MCQ-only and Essay-only filters affect displayed questions.
    - Easy/Medium/Hard level filters affect displayed questions.
    - Timer auto-submit works reliably.
    - Attempts limit works.


