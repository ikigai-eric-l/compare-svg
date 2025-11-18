# SVG Performance Issues from Figma Effects

The Performance Impact of SVG Filters
SVG filters, particularly operations like feBlend, feColorMatrix, and feGaussianBlur, require significant computational resources during rendering. This is especially problematic on mobile devices where processing power and memory are more limited. The impact becomes particularly noticeable when:

Multiple filter operations need to be processed simultaneously

Complex calculations are performed for each pixel

Real-time rendering is required during scroll or animation

Memory usage increases with filter complexity

How Figma Effects Generate Complex SVG Filters
When using Figma's Effects features (Inner shadow, Drop shadow, Layer blur, Background blur), what appears as a simple visual effect in the design tool gets exported as an intricate chain of SVG filters. For example, a simple shape with an inner shadow becomes:

<svg width="75" height="144" viewBox="0 0 75 144" fill="none" xmlns="<http://www.w3.org/2000/svg>">
  <g filter="url(#filter0_i_9015_73050)">
    <path d="M74.4343 90.6911V38.9471H74.4203C73.877 17.3371 57.5574 9.61264e-07 37.5048 0C17.4523 -9.61264e-07 1.1326 17.3371 0.589288 38.9471H0.575333L0.575333 40.0226C0.575333 40.035 0.575317 40.0475 0.575317 40.0599C0.575317 40.0723 0.575333 40.0847 0.575333 40.0972L0.575329 143.548L74.4343 90.6911Z" fill="#090D13" fill-opacity="0.8"/>
  </g>
  <defs>
    <filter id="filter0_i_9015_73050" x="0.575317" y="0" width="73.859" height="143.548" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
      <feOffset/>
      <feGaussianBlur stdDeviation="11.3941"/>
      <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0"/>
      <feBlend mode="normal" in2="shape" result="effect1_innerShadow_9015_73050"/>
    </filter>
  </defs>
</svg>
Instead of what could be a much simpler SVG:

<svg width="75" height="144" viewBox="0 0 75 144" fill="none" xmlns="<http://www.w3.org/2000/svg>">
  <path d="M74.4343 90.6911V38.9471H74.4203C73.877 17.3371 57.5574 9.61264e-07 37.5048 0C17.4523 -9.61264e-07 1.1326 17.3371 0.589288 38.9471H0.575333L0.575333 40.0226C0.575333 40.035 0.575317 40.0475 0.575317 40.0599C0.575317 40.0723 0.575333 40.0847 0.575333 40.0972L0.575329 143.548L74.4343 90.6911Z" fill="#090D13" fill-opacity="0.8"/>
</svg>
The Scale of Our Problem
In our two betting board, there are 576 instances where Figma Effects were used in UI panels. Each instance generates complex SVG filter chains including:

Multiple feBlend operations

feColorMatrix transformations

feGaussianBlur with high stdDeviation values

feComposite operations

Inner shadow effects

This multiplication of complex filter operations has led to significant performance degradation, particularly on mobile devices.

Solutions and Best Practices

1. Avoid SVG Effects
   Replace Figma Effects (Inner shadow, Drop shadow, etc.) with simpler alternatives like strokes

Use basic SVG properties that require minimal computational resources

This significantly reduces rendering overhead, especially on mobile devices

2. Consider WebP, PNG Alternative
   Since our website already prevents user zooming:

Convert complex SVG effects to WebP images

Better performance for static visual elements

Maintains visual fidelity without computational cost

Real World Example: Canvas vs. SVG: Loading Spinner Animation
A canvas-based approach using Pixi.js can maintain a smooth 60 FPS

However, the blur effects applied to SVGs during re-rendering cause significant resource usage, leading to noticeably lower FPS even on desktop machines.

FPS: 60FPS vs ~29FPS

GPU memory: 150MB vs. 435MB

Slack discussions

Conclusion
While Figma's Effects provide powerful design capabilities, their impact on mobile performance can be significant. By implementing these two key solutions - avoiding SVG effects and using WebP alternatives - we can maintain visual quality while ensuring optimal performance across all devices.
