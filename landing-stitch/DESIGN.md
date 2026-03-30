# Design System Strategy: The Architected Trust

## 1. Overview & Creative North Star
The "Architected Trust" is our creative North Star. In the call center and SaaS industry, "trust" is often poorly executed through generic stock photos and rigid blue boxes. We are breaking that template. 

This design system moves away from "Standard Corporate" and toward "Editorial Tech." We treat the TrustMarket interface as a sophisticated, high-end publication. By leveraging **intentional asymmetry**, **over-scaled typography**, and **tonal layering**, we create a digital environment that feels engineered rather than just "built." The goal is a high-conversion experience where the user feels the weight and reliability of the company through the precision of the layout.

---

## 2. Colors & Surface Philosophy
The palette is rooted in a "No-Line" philosophy. To achieve a premium aesthetic, we never use 1px solid borders to define sections. Boundaries are defined through the atmosphere itself.

### The Palette
- **Primary (`#00658d`):** Our foundation of authority.
- **Primary Container (`#00adef`):** The "Action Blue." Reserved strictly for primary CTAs to drive conversion.
- **Surface Hierarchy:** 
    - `surface-container-lowest` (#ffffff) for card backgrounds to pop against subtle sections.
    - `surface-container-low` (#eff4fa) for secondary sectioning.
    - `surface-dim` (#d5dbe1) for deep-set footers or utility bars.

### The Rules of Engagement
*   **The "No-Line" Rule:** Prohibit 1px solid borders for sectioning. Contrast must be achieved by nesting a `surface-container-lowest` card inside a `surface-container-low` section.
*   **Glass & Gradient Rule:** To prevent a "flat" SaaS look, use glassmorphism for navigation bars and floating action cards. Use a `surface` color at 70% opacity with a `24px` backdrop-blur. 
*   **Signature Textures:** Apply a subtle linear gradient from `primary` to `primary-container` (at a 135-degree angle) on hero buttons. This adds "soul" and a tactile, pressed-ink quality to the digital interaction.

---

## 3. Typography: Editorial Authority
We use a dual-typeface system to balance the "Tech" and "Corporate" requirements.

*   **Display & Headlines (Manrope):** While the brand asks for Montserrat's clarity, we utilize **Manrope** for high-level headers to provide a more modern, geometric precision. 
    *   *Scale:* Use `display-lg` (3.5rem) with negative letter-spacing (-0.02em) for hero statements. This creates an "Editorial" impact that feels like a premium magazine.
*   **Body & UI (Inter):** We use **Inter** for all functional text. It is designed for screens and maintains legibility even at `body-sm` (0.75rem).
*   **The Hierarchy Strategy:** Trust is built on clarity. Use `headline-lg` for section titles, but pair them with a `label-md` "kicker" text above them in `primary` color, all-caps, with 0.1em tracking.

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are often "dirty." In this system, depth is a result of light and layering, not artificial drops.

*   **The Layering Principle:** Stack your surfaces. A `surface-container-lowest` element sitting on a `surface-container-high` background creates a natural elevation. 
*   **Ambient Shadows:** If an element must float (like a conversion popup), use a shadow with a 40px blur, 0px offset, and 6% opacity of the `on-surface` color. It should feel like a soft glow of depth, not a silhouette.
*   **The "Ghost Border" Fallback:** If a border is required for accessibility in input fields, use `outline-variant` at 20% opacity. Never use a 100% opaque border; it breaks the fluid "No-Line" aesthetic.

---

## 5. Components
Our components are the building blocks of the TrustMarket experience. They should feel "heavy" and intentional.

*   **Buttons:**
    *   *Primary:* `primary-container` background, `on-primary-container` text. Roundedness: `md` (0.375rem).
    *   *Secondary:* Ghost style using `outline` at 20% opacity. No fill.
*   **Cards:** Forbid divider lines. Use `spacing-8` (2rem) of internal padding and rely on `headline-sm` to start new content clusters.
*   **Input Fields:** Use `surface-container-highest` for the fill. This provides a "recessed" look that suggests the user is "filling into" the platform, increasing the feeling of security.
*   **Trust Badges (Chips):** Use `secondary-container` with `on-secondary-container` text. These should be `full` rounded (pills) to contrast against the sharper `md` corners of the buttons.
*   **Floating Navigation:** The main nav should be a `surface` glassmorphic bar (backdrop-blur: 12px) that stays fixed. This ensures the "TrustMarket" logo is an ever-present anchor.

---

## 6. Do’s and Don’ts

### Do:
*   **Do** embrace white space. Use `spacing-24` (6rem) between major sections to let the "Minimalist" vibe breathe.
*   **Do** use asymmetrical layouts. Place a hero image slightly off-center or overlapping a surface container to break the "Bootstrap" grid feel.
*   **Do** use `tertiary-container` (#e78d18) for micro-interactions like "New Feature" badges or urgent alerts to provide a professional pop of warmth.

### Don't:
*   **Don't** use 1px black or dark grey borders. Ever.
*   **Don't** use standard "drop shadows" (e.g., 0px 2px 4px). They feel dated and cheap.
*   **Don't** use Montserrat for long-form body text. Keep it for headers where its weight can shine; use Inter for readability in the UI.
*   **Don't** clutter the "Value Proposition" section. Use `display-md` and nothing else for the primary hook.