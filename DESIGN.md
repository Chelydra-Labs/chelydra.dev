# Chelydra Labs — Design System & Brand Guidelines

Welcome to the official design documentation for **Chelydra Labs**. This document outlines the visual identity, color systems, typography, and user interface guidelines ensuring a cohesive look and feel across all software projects, web properties, and documentation.

---

## 1. Brand Philosophy

The **Chelydra Labs** identity is built around *Chelydra* (the snapping turtle)—symbolizing resilience, low-level structural stability, and a sharp, defensive technical edge. The official brand motto is **"Hard Shell. Sharp Edge."** 

The visual language is **geometric, blocky, and cybernetic**, bridging the gap between low-level engineering grit and modern full-stack systems architecture. It rejects overly rounded, soft corporate styles in favor of high-contrast, structural angles and tech-forward tones.

---

## 2. Core Assets

### Logo & Mascot
* **File:** `logo.png`
* **Format:** 1:1 Aspect Ratio, High-contrast blocky/vector hybrid.
* **Usage:** GitHub organization avatar, application icons, and favicon variants.

#### Mascot Visual Description
The mascot features a stylized, cybernetic **Common Snapping Turtle (*Chelydra serpentina*)** positioned in a powerful, left-facing profile stance. 

* **Head & Expression:** The head is heavily armored and blocky, featuring a sharp, angular beak and a fierce, tactical expression. The eye glows with a sharp, vibrant amber-orange light, suggesting active processing or power.
* **Carapace (Shell):** The shell is constructed from heavy, geometric plates in a dark steel-blue tone. The ridges of the scutes and the outer rim of the shell are lined with high-contrast, angular amber/gold plating, emphasizing a rigid, shield-like defensive structure.
* **Limbs & Armor:** The legs and thick neck are rendered in a deep tech-green/teal with distinct, blocky segments resembling mechanical or cybernetic armor plating. The joints feature circular, rivet-like gray panels, and each foot terminates in thick, sharp, square-angled claws.
* **Tail:** A thick, heavy tail extends to the right, lined with sharp, jagged triangular spikes along the top ridge to match the formidable look of the turtle's shell.
* **Glow & Separation:** The entire mascot asset is wrapped in a clean, sharp Teal Accent outline, isolating it cleanly from dark backgrounds and giving it a distinct, emblem-like sticker effect.

---

## 3. Color System

The palette features a heavily optimized dark-mode foundation contrasted with sharp cybernetic accents and highly readable neutral tones (as mapped in `watermarked_img_15663655474338550199.png`).

The canvas color (`#14151b`) intentionally matches the logo's own backdrop so the full lockup (mascot + wordmark) blends seamlessly into the page without a visible seam.

### Primary Brand Colors
| Color Name | Hex Code | Purpose / Best Practice |
| :--- | :--- | :--- |
| **Deep Tech Charcoal** | `#14151b` | Default dark application background, canvas backdrop. Matches the logo backdrop for seamless integration. |
| **Steel Blue** | `#2D637A` | Large structural blocks, subtle branding sections, headers. |

### Accent & Action Colors
| Color Name | Hex Code | Purpose / Best Practice |
| :--- | :--- | :--- |
| **Teal Accent** | `#1BC5BA` | Primary interactive elements, CTA buttons, active state indicators. |
| **Gold Warning / Link**| `#FFA500` | Secondary links, inline code highlights, system warnings/alerts. |
| **Tan Secondary Accent**| `#EEDDBB` | Subtitle highlights, tooltips, or stylized light card backgrounds. |

### Neutrals & Interface Colors
| Color Name | Hex Code | Purpose / Best Practice |
| :--- | :--- | :--- |
| **UI Light Background**  | `#F0F4F4` | Light-mode alternate canvas or main body text in deep dark mode. |
| **UI Mid-Tone Panel**   | `#4A6E7D` | Card borders, secondary buttons, component dividers. |
| **Dark UI Text**         | `#2A2A2A` | Primary body text *only* when utilizing light-mode components. |
| **Ultra-Dark Text**      | `#040808` | Text hovers, deep shadows, absolute terminal blackouts. |

---

## 4. Typography

To mirror the blocky, geometric nature of the brand, typography should prioritize clean readability with a distinct developer aesthetic.

* **Primary System/Sans Font:** `Inter`, `Mona Sans`, or system default sans-serif.
  * *Usage:* Main application UI, body copy, navigation links.
* **Monospace / Code Font:** `JetBrains Mono`, `Fira Code`, or `SF Mono`.
  * *Usage:* Code blocks, terminal components, data grids, metrics, and secondary headings.

### Header Scale
* `# H1`: Bold, angular, uppercase tracking recommended for landing pages.
* `## H2`: Medium weight, paired with a subtle **Teal Accent** underline or border-left for documentation.

---

## 5. UI & Component Application Guidelines

> **Dark Mode First:** All interfaces should default to a dark-theme presentation using `#14151b` to maximize the glow and contrast of the Teal and Gold elements.

### Layout & Page Blueprints
* **Asymmetric Hero Split:** For landing pages, pair typography, description, and primary/secondary CTAs side-by-side with the mascot visual over a radial brand glow. Since the mascot image is opaque, it is styled inside a dedicated, solid-backed container framed by tactical cybernetic target brackets in Teal Accent to blend it intentionally into the page layout.
* **Two-Column Sticky Dashboard:** Project detail pages display technical prose in a wide primary column, with download assets (`ReleaseList`), resource link matrices, and repository metadata in a narrow, sticky sidebar column.
* **Canvas Grid Overlay:** Implement a hardware-inspired geometric pattern with `40px` spaced grid lines using a low-opacity `Steel Blue` line color (`rgba(45, 99, 122, 0.04)`) to anchor the cybernetic theme.

### Component Polish
* **Buttons:** Primary buttons use `#1BC5BA` background with `#040808` text. Secondary actions use `#4A6E7D` borders with transparent or low-opacity fills. Hover states should leverage subtle elevations and translations (e.g., arrow slide offsets).
* **Borders & Radii:** Keep corner radii tight (`2px` to `4px` maximum) or completely square (`0px`) to honor the geometric, blocky design language of the logo. Avoid soft, circular pills for standard layout containers.
* **Glassmorphic Panels:** Cards, sticky headers, and navigation panels use translucent dark backgrounds (`rgba(22, 24, 33, 0.75)`) with a light steel-blue border (`rgba(74, 110, 125, 0.22)`) and `backdrop-filter: blur(12px)`.
* **Code Blocks:** Wrap in `#040808` backgrounds with a thin `#2D637A` border. Accent paths or variable highlights should lean into the `#FFA500` gold spectrum.