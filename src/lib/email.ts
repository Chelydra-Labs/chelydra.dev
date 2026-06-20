// Email obfuscation helpers.
//
// The plaintext address is NEVER shipped in the server-rendered HTML.
// Clients reconstruct the mailto: link at runtime from a base64 payload
// decoded by an inline script. A no-JS fallback renders a munged form
// ("turtle [at] chelydra [dot] dev") that is useless to most harvesters
// but still readable by humans.

export function getEmail(): string {
  return process.env.CONTACT_EMAIL ?? 'turtle@chelydra.dev';
}

// Base64 of the plaintext address. Safe to ship in data-* attributes.
// Computed at request time on the server so the source never appears in
// the repo or the bundle.
export function emailBase64(): string {
  return Buffer.from(getEmail(), 'utf8').toString('base64');
}

// Human-readable munged form for the <noscript> fallback.
export function emailMunged(): string {
  return getEmail().replace('@', ' [at] ').replace(/\./g, ' [dot] ');
}
