Safari compatibility issues:
not support SMIL animations



<svg xmlns="<http://www.w3.org/2000/svg>" width="200" height="200" viewBox="0 0 200 200">
  <circle cx="50" cy="50" r="20" fill="red">
    <animate attributeName="r" values="20;40;20" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>
filter, mask-type, paint-order



<svg xmlns="<http://www.w3.org/2000/svg>" width="200" height="200" viewBox="0 0 200 200">
  <!-- filter -->
  <defs>
    <filter id="blur">
      <feGaussianBlur stdDeviation="5" />
    </filter>
  </defs>
  <rect x="100" y="20" width="80" height="80" fill="blue" filter="url(#blur)" />
  <!-- mask-type -->
  <mask id="myMask" mask-type="alpha">
    <circle cx="150" cy="150" r="30" fill="white" />
  </mask>
  <rect x="120" y="120" width="60" height="60" fill="green" mask="url(#myMask)" />
  <!-- paint-order -->
  <text x="10" y="180" font-size="20" stroke="black" stroke-width="2" fill="white" paint-order="stroke fill">
    Paint Order Text
  </text>
</svg>
 

React render SVG in TSX file
Using a large SVG file converted to TSX can lead to performance issues in React-based websites. This approach increases the JavaScript burden, as it requires processing a large amount of JSX on each render. Here are some suggestions to improve performance:

Use external SVG files:
Save the SVG as a separate file and reference it using an <img> tag or SVG's <use> element. This reduces JavaScript processing.

Optimize SVG:
Use tools like SVGO to optimize SVG files, removing unnecessary elements and attributes.

Lazy loading:
If the SVG isn't immediately visible, consider using lazy loading techniques.

Split SVG:
If possible, split large SVGs into smaller pieces, loading and rendering only when need