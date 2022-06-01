---
layout: page 
title: Software
permalink: /software/
---

<div class="home">
  {% assign sws = site.categories.software %}
  <ul class="post-list">
    {%- for sw in sws -%}
      <li>
        <a class="post-link" href="{{ sw.url | relative_url }}">
          {{ sw.title | escape }}
        </a>
        {{ sw.excerpt }}
      </li>
    {%- endfor -%}
  </ul>
</div>

Programming paradigms
-------------------------------

I like exploring emerging programming paradigms (especially around concurrent programming or applications with hard latency constraints) and learning about comparative strengths and weaknesses of general-purpose programming languages (e.g., C++, Python, Java, Go, Rust, Haskell, Common Lisp).  For my projects, I have used the following.

- **Systems Programming:** [modern C++](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines), C, UNIX/Linux
- **Scripting:** Python, Bash
- **Web programming:** HTML, Javascript, CSS
- **Technical writing:** Latex, Markdown
- **Software-defined radio:** [libiio](https://github.com/analogdevicesinc/libiio), [bladeRF](https://nuand.com/bladeRF-doc/libbladeRF/)
