---
layout: page 
title: Miscellaneous
permalink: /misc/
---

Volunteer activity/service
--------------------------

<div class="home">
  {% assign acts = site.categories.volunteer %}
  <ul class="post-list">
    {%- for act in acts -%}
      <li>
        <a class="post-link" href="{{ act.url | relative_url }}">
          {{ act.title | escape }}
        </a>
        {{ act.excerpt }}
      </li>
    {%- endfor -%}
  </ul>
</div>
