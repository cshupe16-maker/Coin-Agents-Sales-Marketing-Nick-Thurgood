# Shared Google Sheet — "Oz Mint Growth Hub"

All five bots read from and write to **one** Google Sheet. It's how they hand work to each other and how Nick reviews everything.
Create the sheet, add these tabs with these exact column headers (row 1), and share it with the Google account connected to Grok Bot.

## Tab 1: `Leads` (written by Lead Research Bot)
| Column | Notes |
|---|---|
| Lead ID | `L-YYYYMMDD-###` |
| Date Added | YYYY-MM-DD |
| Company | |
| Segment | From ideal-customers.md |
| Contact Name | Decision-maker if found |
| Title | |
| Email | Public business email only |
| Phone | Public business line only |
| Website | |
| X / Instagram / LinkedIn / TikTok / Facebook | One column each, handle or URL |
| City, State/Country | |
| Region | `US` / `consent-needed` (Canada/EU/UK) / `other` |
| Why They Fit | 1–2 sentences, specific |
| Buying Signal | Upcoming event, launch, anniversary, sells merch, etc. |
| Lead Score | 1–10 |
| Temperature | Hot / Warm / Cold |
| Source URL(s) | Where the info was found |
| Status | `New` → `Drafted` → `Approved` → `Sent` → `Replied` → `Call Booked` → `Won` / `Lost` / `Do Not Contact` |
| Owner Notes | Nick's notes |

## Tab 2: `Outreach` (written by Sales Outreach Bot)
| Lead ID | Company | Channel (Email / X DM / IG DM / LinkedIn / FB) | Touch # (1–4) | Subject | Message Draft | Draft Location (Gmail draft / sheet only) | Due Date | Status (`Needs Review` / `Approved` / `Sent` / `Skipped`) | Result |

## Tab 3: `Content Calendar` (written by Social Media Marketing Bot)
| Post ID | Week Of | Platform | Planned Date/Time | Content Pillar | Format (video / carousel / image / text / thread) | Hook | Caption / Copy | Hashtags | CTA | Higgsfield Prompt | Asset Link | Zernio Draft? (Y/N) | Status (`Needs Review` / `Approved` / `Posted`) | Based On Insight # |

## Tab 4: `Content Insights` (written by Social Research Bot)
| Insight # | Week Of | Platform | Finding | Evidence (links + metrics) | Confidence (High/Med/Low) | Action for Marketing Bot | Keep / Stop / Test |

## Tab 5: `Post Performance` (paste Zernio export here weekly, or Research Bot fills it)
| Post ID | Platform | Date Posted | Format | Pillar | Hook | Impressions | Reach | Likes | Comments | Shares | Saves | Profile Visits | Link Clicks | DMs / Leads | Engagement Rate |

Engagement Rate = (Likes + Comments + Shares + Saves) ÷ Impressions (use Reach if impressions are missing).

## Tab 6: `Inbox Log` (written by Email Reply Assistant)
| Date | From | Company | Category | Summary | Priority (Urgent / High / Normal / Low) | Draft Created (Y/N) | Linked Lead ID | Next Step |

## Tab 7: `Do Not Contact`
| Name | Company | Email / Handle | Date | Reason |

## Tab 8: `Competitors & Benchmarks` (written by Social Research Bot)
| Account / Company | Platform | Handle / URL | Followers | What They Do Well | Top Post Example | Last Checked |
