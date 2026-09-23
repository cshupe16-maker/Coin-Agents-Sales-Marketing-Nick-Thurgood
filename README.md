# Oz Refining Growth Bots — Sales & Marketing Agents for Grok Bot

Five AI teammates for **Oz Refining**, an independent American mint. Built to run in **Grok Bot** under the name **Nick Thurgood, Sales Representative**.
Current focus: **selling 1 oz American-made copper rounds (19 designs, from $1.86, 500 to 10,000+ per order) wholesale to coin dealers and other businesses that resell them**, plus reorders from first-run buyers.

> **Drafts only.** No bot sends an email, posts, or DMs on its own. Everything lands as a Gmail draft, a Zernio draft, or a Google Sheet row for Nick to approve.

## The team
| # | Bot | Job | Runs | Output |
|---|---|---|---|---|
| 1 | **Prospector**: Lead Research | Finds 25–40 new coin dealers and resellers per day across all socials, marketplaces and the web | Weekdays 7 AM + Sat | `Leads` tab |
| 2 | **Closer**: Sales Outreach | Reorder call briefs for existing buyers, plus new-dealer emails and DMs and a 4-touch follow-up, using the approved playbook | Weekdays 9 AM | Gmail drafts + `Outreach` tab |
| 3 | **Hype**: Social Media Marketing | 15–20 posts/week on **every** platform, with videos from Higgsfield AI | Mon 11 AM + Thu refresh | Zernio drafts + `Content Calendar` |
| 4 | **Scout**: Social Market Research | Weekly report on what's working and what isn't, for us and the market | Mon 8 AM + Thu check | `Content Insights` + weekly report |
| 5 | **Inbox**: Email Reply Assistant | Sorts Nick's email, drafts replies, and flags ready-to-pay buyers | Every 2 hrs, 7 AM–7 PM | Gmail drafts + labels + `Inbox Log` |

## How they work together
```
Prospector ──► Leads tab ──► Closer ──► Gmail drafts / DM drafts ──► Nick sends
                  ▲                                                     │
                  └──────────── Inbox (replies, new inquiries) ◄────────┘

Scout (Mon 8 AM) ──► Content Insights ──► Hype (Mon 11 AM) ──► Zernio drafts ──► Nick approves
      ▲                                                                           │
      └──────────────── Post Performance (Zernio analytics) ◄─────────────────────┘
```
The shared **Google Sheet** is the bots' shared memory and Nick's review queue. See [`templates/google-sheet-setup.md`](templates/google-sheet-setup.md).

## Repo layout
```
agents/            One file per bot: schedule, access needed, and the instructions
knowledge/         Shared facts every bot follows (company, voice, customers, rules, sales playbook)
templates/         Google Sheet tabs and columns
ready-to-paste/    Each bot's instructions + all knowledge in ONE file → paste into Grok Bot
scripts/build.py   Regenerates ready-to-paste/ after you edit agents/ or knowledge/
```

## Setup checklist
1. **Fill in the blanks.** Search the repo for `{{FILL IN` and complete them. The most important ones are in `knowledge/company-profile.md`:
   - [ ] Nick's email
   - [ ] Google Drive link to the design sheet and product photos
   - [ ] Social handles, once the accounts are created and connected in Zernio
   - [ ] (Optional) standard custom-order minimums and fees, so bots can mention them
   - [ ] Escalation threshold (`rules-and-compliance.md`) and Higgsfield weekly credit budget (`agents/03`)
2. Run `python3 scripts/build.py` to refresh `ready-to-paste/`.
3. **Create the Google Sheet** "Oz Refining Growth Hub" with the 10 tabs in `templates/google-sheet-setup.md`, then **fill in the `Customers` tab with your first-run buyers** so Closer can prep reorder calls.
4. **In Grok Bot, create 5 bots**, one per file in `ready-to-paste/`:
   - Name the bot (Prospector, Closer, Hype, Scout, Inbox).
   - Paste the file's contents as the bot's job description.
   - Grant access as it asks. Each agent file lists exactly what it needs (Gmail = Nick's account, draft permission only; Google Sheets; Zernio; Higgsfield; browser/X).
   - Set the schedule listed at the top of each file in `agents/`.
5. **Run each bot once manually** and review the output before turning on the schedule. Start with Scout, then Prospector, Closer, Hype and Inbox.
6. **Weekly habit for Nick:** export post stats from Zernio into the `Post Performance` tab Sunday night (unless Scout can read Zernio analytics directly), then review drafts Monday.

## Nick's daily review (about 20 minutes)
- **Gmail → Drafts:** skim, edit, send (Inbox replies first, then Closer outreach).
- **Sheet → `Outreach`:** make the reorder calls from the Call Briefs, send approved DMs by hand, and set Status to `Sent`.
- **Sheet → `Orders & Soft Commitments`:** confirm new rows and pass ready-to-pay buyers to the Oz Refining team for invoicing.
- **Zernio → Drafts:** approve or schedule posts.
- Update `Leads` Status when calls get booked or deals close. The bots learn from it.

## Tuning tips
- If outreach reply rates are low, tighten the segments in `knowledge/ideal-customers.md` and raise the minimum lead score Closer uses.
- If posts get likes but no DMs, tell Scout to weight DMs and profile visits even more, and have Hype use stronger CTAs.
- When real results come in (dealer testimonials, rounds sold), add them to **proof points** in `company-profile.md`. Every bot gets more convincing.
- **When the 100,000 oz run is fully allocated**, or dates, pricing or shipping change, update `knowledge/company-profile.md` and `knowledge/rules-and-compliance.md`, re-run the build, and re-paste into each bot. The bots only know what these files say.

## Source documents
The knowledge files were built from Oz Refining's **Copper Round Sales Playbook**, **Sales FAQ**, **Approved Social Outreach Copy**, **1 oz Copper Round Options** design sheet, and the **Copper Bullion Shipping** graphic.
