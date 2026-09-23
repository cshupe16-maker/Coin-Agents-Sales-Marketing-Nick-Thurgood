# Shared Google Sheet — "Oz Refining Growth Hub"

All five bots read from and write to **one** Google Sheet. It's how they hand work to each other and how Nick reviews everything.
Create the sheet, add these tabs with these exact column headers in row 1, and share it with the Google account connected to Grok Bot.
If Oz Refining already has an order spreadsheet (the one the Sales FAQ mentions), keep using it for orders. Link it in the `Orders & Soft Commitments` tab, and give bots **read-only** access unless Nick says otherwise.

## Tab 1: `Customers` (existing buyers; Nick fills this in first, and bots update it)
| Customer ID | Business | Contact Name | Phone | Email | Facebook / Other | First Order Qty | First Order Design | Order Condition / Satisfaction | Est. Qty Remaining | Retail Price | Est. Sales / Month | Reorder Class (30/60/90) | Last Contact | Next Follow-Up | Soft Commitment Qty | Preferred Design | Objections / Competitor Info / Feedback | Perks They Value | Referrals Given |

## Tab 2: `Leads` (new prospects; written by Lead Research Bot)
| Lead ID (`L-YYYYMMDD-###`) | Date Added | Business | Segment | Contact Name | Title | Email (public business only) | Phone (public business only) | Website | Facebook | Instagram | X | TikTok | Whatnot / eBay / Etsy | Other | City, State | Region (`US` / `non-US`) | Why They Fit | Buying Signal | Designs That Fit | Lead Score (1–10) | Temperature | Source URL(s) | Status | Owner Notes |

**Status values:** `New` → `Drafted` → `Approved` → `Sent` → `Replied` → `Call Set` → `Soft Commit` → `Invoiced` → `Paid` / `Lost` / `Do Not Contact` / `Needs Research`

## Tab 3: `Outreach` (written by Sales Outreach Bot)
| Lead/Customer ID | Business | Type (New Dealer / Reorder / Referral) | Channel (Email / FB Messenger / FB Group / IG DM / X DM / Text / Call Brief) | Touch # (1–4) | Subject | Message Draft or Call Brief | Suggested Quantity | Draft Location | Due Date | Status (`Needs Review` / `Approved` / `Sent` / `Skipped`) | Result |

## Tab 4: `Orders & Soft Commitments` (bots draft rows; Nick confirms)
| Date | Customer / Business | Contact | Email | Phone | Billing Address | Shipping Address | Design(s) | Quantity | Est. Price / Round | Est. Shipping (per policy) | Preferred Payment (e-check / wire / mailed check) | Type (Soft Commit / Ready to Pay) | Confirmation Date (end Oct 2026) | Status | Notes |

**Never put banking details in this sheet.**

## Tab 5: `Content Calendar` (written by Social Media Marketing Bot)
| Post ID | Week Of | Platform | Planned Date/Time | Content Pillar | Design(s) Featured | Format | Hook | Caption / Copy | Hashtags | CTA | Higgsfield Prompt | Asset Link | Zernio Draft? (Y/N) | Status (`Needs Review` / `Approved` / `Posted`) | Based On Insight # |

## Tab 6: `Content Insights` (written by Social Research Bot)
| Insight # | Week Of | Platform | Finding | Evidence (links + metrics) | Confidence (High/Med/Low) | Action for Marketing Bot | Keep / Stop / Test |

## Tab 7: `Post Performance` (paste the Zernio export weekly, or the Research Bot fills it)
| Post ID | Platform | Date Posted | Format | Pillar | Design(s) | Hook | Impressions | Reach | Likes | Comments | Shares | Saves | Profile Visits | Link Clicks | DMs / Quantity Inquiries | Engagement Rate |

Engagement Rate = (Likes + Comments + Shares + Saves) ÷ Impressions (use Reach if impressions are missing).

## Tab 8: `Inbox Log` (written by Email Reply Assistant)
| Date | From | Business | Category | Summary | Quantity / Design Mentioned | Priority (Urgent / High / Normal / Low) | Draft Created (Y/N) | Linked ID | Next Step |

## Tab 9: `Do Not Contact`
| Name | Business | Email / Handle / Phone | Date | Reason |

## Tab 10: `Competitors & Benchmarks` (written by the Research Bot and from sales conversations)
| Company / Account | Type (Mint / Dealer / Creator) | Platform / URL | Made in USA or Imported | Known Price / Terms | Followers | What They Do Well | Top Post Example | Source | Last Checked |
