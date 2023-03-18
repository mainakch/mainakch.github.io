---
layout: page 
title: Papers
permalink: /papers/
---

<div class="home">
  {% assign papers = site.categories.paper %}


  {%- if papers.size > 0 -%}
    {%- if page.list_title -%}
      <h2 class="post-list-heading">{{ page.list_title }}</h2>
    {%- endif -%}

    <h3>
      <a href="/assets/sorted_references.bib"> Bibtex </a> 
    </h3>

    The following list excludes publications / patents which have not undergone technical peer review.

    <ul class="post-list">
      {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
      {%- for paper in papers -%}
      <li>
        <span class="post-meta">{{ paper.date | date: date_format }}</span>
          <a class="post-link" href="{{ paper.url | relative_url }}">
            {{ paper.title | escape }}
          </a>
        {%- if site.show_excerpts -%}
          {{ paper.excerpt }}
        {%- endif -%}
      </li>
      {%- endfor -%}
    </ul>

  {%- endif -%}

</div>
