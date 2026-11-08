#!/bin/zsh
# Generate card images with the Codex CLI (ChatGPT image generation), 3 at a time, one folder per card.
#
# Usage: gen_cards.sh JOBS.tsv OUT_DIR
#   JOBS.tsv has one line per card, tab-separated: number <TAB> prompt file <TAB> style reference image <TAB> subject image
#   (the prompt file comes from build_prompt.py). Results land in OUT_DIR/c<number>/card-<number>.png, with the full
#   Codex log in run.log next to it. Re-running a number overwrites that folder, so move rejects aside first.
#
# Needs: `codex` on PATH, logged in with ChatGPT (`codex login status`), and the image_generation feature on
# (`codex features list`). Each image takes about 2 minutes.
set -u
JOBS=$1; OUT=$2; PAR=${PAR:-3}
mkdir -p "$OUT"
one() {
  local n=$1 p=$2 ref=$3 subj=$4 d="$OUT/c$1"
  mkdir -p "$d"; cp "$p" "$d/task.txt"
  printf '\nImage 1 (layout/style reference) and image 2 (the subject) are attached. Generate the image, then save the generated image file into the current directory as card-%s.png. Do nothing else.\n' "$n" >> "$d/task.txt"
  (cd "$d" && timeout 900 codex exec --skip-git-repo-check --sandbox workspace-write -i "$ref" -i "$subj" -o last.txt - < task.txt > run.log 2>&1)
  [[ -f "$d/card-$n.png" ]] && echo "$n ok" || echo "$n FAILED (see $d/run.log)"
}
while IFS=$'\t' read -r n p ref subj; do
  [[ -z "$n" || "$n" == \#* ]] && continue
  one "$n" "$p" "$ref" "$subj" &
  while (( $(jobs -r | wc -l) >= PAR )); do sleep 5; done
done < "$JOBS"
wait
