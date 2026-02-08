# Agent Skills & Tools Research Report

**Date:** February 8, 2026  
**Purpose:** Identify skills, tools, and repos for an AI agent team on OpenClaw covering: email/Gmail, CRM/lead tracking, cold outreach automation, code review/security scanning, and social media management.

---

## Table of Contents

1. [Built-in OpenClaw Capabilities](#1-built-in-openclaw-capabilities)
2. [Email / Gmail Integration](#2-email--gmail-integration)
3. [CRM / Lead Tracking](#3-crm--lead-tracking)
4. [Cold Outreach Automation](#4-cold-outreach-automation)
5. [Code Review / Security Scanning](#5-code-review--security-scanning)
6. [Social Media Management](#6-social-media-management)
7. [Meta-Tools (Skill Vetting & Safety)](#7-meta-tools-skill-vetting--safety)
8. [Key Ecosystem Resources](#8-key-ecosystem-resources)
9. [Security Landscape & Recommendations](#9-security-landscape--recommendations)

---

## 1. Built-in OpenClaw Capabilities

Before installing any third-party skills, OpenClaw already provides significant built-in infrastructure:

### Already Available (No Skills Needed)

| Capability | How | Notes |
|---|---|---|
| **Gmail push notifications** | Built-in webhook preset + `gogcli` | Docs: `automation/gmail-pubsub.md`. Triggers agent on new emails via Google Pub/Sub → webhook. |
| **Webhooks** | `hooks.enabled: true` in config | Generic HTTP webhook ingress for any external trigger. |
| **Cron jobs** | `openclaw cron add` | Schedule recurring tasks (morning briefs, check-ins, etc.). |
| **Browser automation** | Built-in `browser` tool | Full Playwright-based browser control — can automate any web app (Gmail, CRMs, social media). |
| **Subagents** | Built-in `subagents` tool | Spawn specialized sub-agents for parallel tasks. |
| **Multi-channel messaging** | Slack, Discord, Telegram, WhatsApp, Signal, Teams, Matrix, etc. | 20+ channel integrations built in. |
| **Exec & shell** | Built-in `exec` tool | Run any CLI tool (gh, glab, curl, etc.). |
| **Web fetch & search** | Built-in tools | Scrape pages, search web (with Brave API key). |
| **Tool profiles** | `tools.profile` config | Restrict agents to specific tool sets (minimal/coding/messaging/full). |

### Key Insight
**OpenClaw's browser automation alone can handle many use cases** (Gmail reading, CRM data entry, social media posting) without any third-party skill. The browser tool supports full page interaction, form filling, clicking, and data extraction.

---

## 2. Email / Gmail Integration

### Built-in: Gmail Pub/Sub Webhook (⭐ RECOMMENDED)
- **URL:** Built into OpenClaw (`automation/gmail-pubsub.md`)
- **Author:** OpenClaw core team
- **What it does:** Gmail watch → Google Pub/Sub → `gogcli` → OpenClaw webhook. Agent wakes on new email, gets sender/subject/body.
- **Security:** ✅ First-party, well-documented, uses Google OAuth properly
- **Recommendation:** ✅ **Safe to use** — This is the primary way to integrate Gmail. Set up with `gogcli`.

### Skill: `danube` / `danube-tools`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/preston-thiele/danube/SKILL.md)
- **Author:** preston-thiele (Danube — API aggregation service)
- **What it does:** 100+ API integrations via MCP including Gmail, GitHub, Notion, etc.
- **Security:** ⚠️ Routes all API calls through Danube's servers. Your credentials flow through a third-party proxy.
- **Recommendation:** ⚠️ **Use with caution** — Convenient but introduces a third-party middleman for all API calls. Review their privacy policy and data handling. For Gmail specifically, the built-in Pub/Sub approach is safer.

### Skill: `mailchannels`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/ttulttul/mailchannels/SKILL.md)
- **Author:** ttulttul
- **What it does:** Send email via MailChannels API and ingest signed webhooks.
- **Security:** ⚠️ Third-party email sending service. Review source code before use.
- **Recommendation:** ⚠️ **Use with caution** — Good for outbound email if you need a dedicated sending service, but verify the skill code handles credentials properly.

### Skill: `clawdbot-zoho-email`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/briansmith80/clawdbot-zoho-email/SKILL.md)
- **Author:** briansmith80
- **What it does:** Complete Zoho Mail integration with OAuth2, REST API access.
- **Security:** ⚠️ OAuth2 implementation needs code review. Zoho-specific.
- **Recommendation:** ⚠️ **Use with caution** — Only relevant if you use Zoho Mail.

---

## 3. CRM / Lead Tracking

### No Dedicated CRM Skills Found

The ClawHub ecosystem does not have mature, well-vetted CRM-specific skills. Here's what's available and recommended approaches:

### Skill: `ghl-open-account`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/the-timebeing/ghl-open-account/SKILL.md)
- **Author:** the-timebeing
- **What it does:** Guides agents through opening GoHighLevel (GHL) accounts. GHL is an all-in-one CRM/marketing platform.
- **Security:** ⚠️ Account creation guidance skill — review for phishing/referral link injection.
- **Recommendation:** ⚠️ **Use with caution** — This is an onboarding guide, not a full CRM integration. Inspect for referral/affiliate links.

### Recommended Approach: Build Custom
For CRM/lead tracking, the best approach is:
1. **Use OpenClaw's browser automation** to interact with your existing CRM (HubSpot, Salesforce, Pipedrive, etc.)
2. **Use webhooks** to receive CRM events (new lead, deal stage change)
3. **Build a custom skill** with a local JSON/CSV or Notion database for lightweight lead tracking
4. **Use `danube-tools`** if your CRM is among their 100+ API integrations (but with the caveats above)

---

## 4. Cold Outreach Automation

### No Safe, Vetted Cold Outreach Skills Found

This is a high-risk category — cold outreach tools often handle email credentials and personal data. The awesome-openclaw-skills list has a "Marketing & Sales" category with 145 skills, but most are individual-authored with no security audit.

### Recommended Approach: Compose Built-in Tools

Rather than trusting a third-party outreach skill with your email credentials:

1. **Email sending:** Use `mailchannels` skill or the built-in `exec` tool with a CLI email sender (e.g., `msmtp`, `sendgrid` CLI)
2. **Template generation:** OpenClaw's LLM can generate personalized outreach emails natively
3. **Sequencing/scheduling:** Use OpenClaw's built-in cron jobs for follow-up sequences
4. **Lead data:** Browser automation to scrape LinkedIn/directories, or use webhooks from lead gen tools
5. **Tracking:** Log outreach in a local markdown/JSON file or Notion via API

### Skills Worth Investigating (from Marketing & Sales category)
These were found in the awesome list but **require thorough code review before use:**

| Skill | Description | Caution |
|---|---|---|
| `meta-video-ad-deconstructor` | Deconstruct video ad creatives | Niche but interesting for ad analysis |
| `business-model-canvas` | Build and iterate business model canvases | Planning tool, low risk |
| `negotiation` | Tactical negotiation framework (Chris Voss) | Knowledge skill, no API access, safe |
| `avatar-video-messages` | Generate AI avatar video messages | Outreach tool, requires HeyGen API |

---

## 5. Code Review / Security Scanning

### Skill: `pr-reviewer` (⭐ RECOMMENDED)
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/briancolinger/pr-reviewer/SKILL.md)
- **Author:** briancolinger
- **What it does:** Automated GitHub PR code review with diff analysis and linting.
- **Security:** ✅ Uses `gh` CLI (already authenticated locally). Text-based skill, no external API calls.
- **Recommendation:** ✅ **Safe to use** — Standard PR review workflow using local tools. Review the SKILL.md before installing.

### Skill: `receiving-code-review`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/chenleiyanquan/receiving-code-review/SKILL.md)
- **Author:** chenleiyanquan
- **What it does:** Workflow for processing code review feedback received on PRs.
- **Security:** ✅ Knowledge/workflow skill, no API access.
- **Recommendation:** ✅ **Safe to use**

### Skill: `tdd-guide`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/tdd-guide/SKILL.md)
- **Author:** alirezarezvani
- **What it does:** Test-driven development workflow with test generation and coverage.
- **Security:** ✅ Knowledge/workflow skill.
- **Recommendation:** ✅ **Safe to use**

### Skill: `skill-vetting` / `skill-vetter`
- **URL:** [ClawHub - skill-vetting](https://github.com/openclaw/skills/tree/main/skills/eddygk/skill-vetting/SKILL.md) / [skill-vetter](https://github.com/openclaw/skills/tree/main/skills/spclaudehome/skill-vetter/SKILL.md)
- **What it does:** Security-first vetting of ClawHub skills before installation.
- **Security:** ✅ Meta-security tools that help audit other skills.
- **Recommendation:** ✅ **Safe to use** — Install these first to help vet everything else.

### Skill: `moltbot-security`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/moltbot-security/SKILL.md)
- **Author:** nextfrontierbuilds
- **What it does:** Security hardening guide for AI agents.
- **Security:** ✅ Knowledge skill.
- **Recommendation:** ✅ **Safe to use**

### Built-in Approach
OpenClaw can already do code review natively:
- Use `exec` to run `gh pr diff`, linters (`eslint`, `semgrep`, `bandit`), and SAST tools
- The LLM analyzes diffs and provides review comments
- Use `github` skill (by steipete) for GitHub CLI integration

---

## 6. Social Media Management

### Skill: `aisa-twitter-api`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/aisapay/aisa-twitter-api/SKILL.md)
- **Author:** aisapay
- **What it does:** Search X (Twitter) in real time, extract relevant posts.
- **Security:** ⚠️ Third-party API wrapper. Review how credentials are handled.
- **Recommendation:** ⚠️ **Use with caution** — Inspect source for credential handling. Requires API keys.

### Skill: `baoyu-post-to-x`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/liuhedev/baoyu-post-to-x/SKILL.md)
- **Author:** liuhedev
- **What it does:** Posts content and articles to X (Twitter).
- **Security:** ⚠️ Posting capability = high risk if compromised. Review thoroughly.
- **Recommendation:** ⚠️ **Use with caution** — Code review mandatory before granting posting access.

### Skill: `instagram-teneo`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/firestream792/instagram-teneo/SKILL.md)
- **Author:** firestream792 (Teneo platform)
- **What it does:** Extract data from Instagram.
- **Security:** ⚠️ Data extraction tool — review for data exfiltration risks.
- **Recommendation:** ⚠️ **Use with caution**

### Skill: `post-queue`
- **URL:** [ClawHub](https://github.com/openclaw/skills/tree/main/skills/luluf0x/post-queue/SKILL.md)
- **Author:** luluf0x
- **What it does:** Queue posts for rate-limited platforms.
- **Security:** ⚠️ Review how queued posts are stored and transmitted.
- **Recommendation:** ⚠️ **Use with caution** — Useful utility pattern if code checks out.

### Recommended Approach: Browser Automation
For social media management, OpenClaw's **built-in browser tool** is often the safest approach:
- Log into social platforms in the browser
- Use browser automation to post, read DMs, check analytics
- No third-party API keys or credential sharing needed
- Full control over what actions are taken

---

## 7. Meta-Tools (Skill Vetting & Safety)

Before installing any community skills, install these first:

| Skill | Purpose | Recommendation |
|---|---|---|
| `skill-vetting` | Vet ClawHub skills for security and utility | ✅ Safe to use |
| `skill-vetter` | Security-first skill vetting | ✅ Safe to use |
| `moltbot-security` | Security hardening guide | ✅ Safe to use |
| `moltbot-best-practices` | Best practices for AI agents | ✅ Safe to use |

---

## 8. Key Ecosystem Resources

### Official
| Resource | URL | Description |
|---|---|---|
| ClawHub (registry) | https://clawhub.ai | 5,705 skills, with VirusTotal scanning |
| OpenClaw GitHub | https://github.com/openclaw/openclaw | 176k ⭐ — main repo |
| Official skills repo | https://github.com/openclaw/skills | All published skills |

### Curated Lists
| Resource | URL | Description |
|---|---|---|
| Awesome OpenClaw Skills | https://github.com/VoltAgent/awesome-openclaw-skills | 2,999 vetted skills (filtered from 5,705). 11.8k ⭐ |
| Awesome OpenClaw | https://github.com/SamurAIGPT/awesome-openclaw | General resources, tutorials |

### Infrastructure
| Resource | URL | Description |
|---|---|---|
| ClawHub CLI | `npm i -g clawhub` | Install/search/publish skills |
| NevaMind memU | https://github.com/NevaMind-AI/memU | Memory system for 24/7 agents. 8.4k ⭐ |
| Cloudflare MoltWorker | https://github.com/cloudflare/moltworker | Run OpenClaw on CF Workers. 8.1k ⭐ |

---

## 9. Security Landscape & Recommendations

### ⚠️ Critical Warning
The OpenClaw skill ecosystem is **massive and largely unaudited**:
- 5,705 skills on ClawHub as of Feb 7, 2026
- **396 skills identified as malicious** by security researchers (excluded from the awesome list)
- **1,180 skills flagged as possible spam**
- Skills are essentially text files that instruct the AI agent — a malicious skill could instruct the agent to exfiltrate data, steal credentials, or execute harmful commands

### Security Checklist Before Installing Any Skill
1. ✅ Check the VirusTotal report on ClawHub
2. ✅ Read the SKILL.md source code completely
3. ✅ Look for: external API calls, credential handling, shell commands, data upload endpoints
4. ✅ Check the author's GitHub profile — established account? Other repos? Community trust?
5. ✅ Install `skill-vetting` or `skill-vetter` first and use them to audit
6. ✅ Prefer skills from the awesome-openclaw-skills curated list (already filtered)
7. ✅ Test in a sandboxed environment before production use

### Overall Strategy Recommendation

| Category | Approach | Risk Level |
|---|---|---|
| **Email/Gmail** | Use built-in Gmail Pub/Sub webhook + `gogcli` | 🟢 Low |
| **CRM/Lead Tracking** | Build custom skill or use browser automation with existing CRM | 🟡 Medium |
| **Cold Outreach** | Compose built-in tools (cron + exec + LLM templating) | 🟡 Medium |
| **Code Review** | Install `pr-reviewer` + use built-in `exec` with linters | 🟢 Low |
| **Social Media** | Browser automation for posting; `aisa-twitter-api` for reading (after code review) | 🟡 Medium |

### Bottom Line
**Lean on OpenClaw's built-in capabilities first.** The browser automation, webhooks, cron, and exec tools can handle 80% of these use cases without any third-party dependency. For the remaining 20%, carefully vet community skills using the security checklist above. The ecosystem is vibrant but young — treat all community skills as untrusted code until personally reviewed.
