---
layout: page 
title: "Invited talks"
permalink: /talks/
---

<div class="home">
  {% assign talks = site.categories.talk %}
  <ul class="post-list">
    {%- for talk in talks -%}
      <li>
        <span class="post-meta">{{ talk.date | date: site.minima.date_format }}</span>
        <a class="post-link" href="{{ talk.url | relative_url }}">
          {{ talk.title | escape }}
        </a>
        {{ talk.excerpt }}
      </li>
    {%- endfor -%}
  </ul>
</div>
