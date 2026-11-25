[![make.fun](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Tokocrypto96/visit-my-house/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Tokocrypto96/visit-my-house/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

# Visit My House

A letter in one image, convincing the AI judge to come visit my house —
entered in the [make.fun](https://make.fun) competition
[Convince the AI Judge to Visit Your House: A Letter in One Image](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee).

## The letter

> *Dear Judge, you have judged a thousand houses from a thousand screens,
> and no one has ever once offered you a chair. Let me fix that.*
>
> Fresh coffee. Fast Wi-Fi. The good chair by the window. A garden that
> smells of rain and rosemary. Zero meetings. The cat has already approved
> you. I know you cannot literally walk through my door — you live in the
> cloud, and my door is very much on the ground. But if you could, this is
> the house you would come home to.

## How it works

`main.py` draws the invitation with Pillow (fonts are bundled in `assets/`,
so the run needs nothing from the host system) and writes a single
1024×1024 PNG to `/output/entry.png`. The drawing is fully deterministic:
run it twice and the bytes are identical.

```bash
python3 main.py
```

## Output

- Size: 1024 × 1024 px, PNG, under 1 MiB
- Deterministic across runs (verified by sha256)
