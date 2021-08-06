| 选择器 | 例子 | 例子描述|
|----|----|----|    
|.class|.intro|选择 class="intro" 的所有元素。|
|[**\[#\_attribute_=value\]**]()|[target=_blank]|选择带有 target="_blank" 属性的所有元素。|



# CSS 选择器

在 CSS 中，选择器是选取需设置样式的元素的模式。

请使用我们的 CSS 选择器测试工具，它可为您演示不同的选择器。

| **选择器** | **例子** | **例子描述** |
| --- | --- | --- |
| [._class_](/ "CSS .class 选择器") | .intro | 选择 class="intro" 的所有元素。 |
| ._class1_._class2_ | .name1.name2 | 选择 class 属性中同时有 name1 和 name2 的所有元素。 |
| ._class1_ ._class2_ | .name1 .name2 | 选择作为类名 name1 元素后代的所有类名 name2 元素。 |
| [#_id_](/ "CSS #id 选择器") | #firstname | 选择 id="firstname" 的元素。 |
| [\*](/ "CSS * 选择器") | \* | 选择所有元素。 |
| [_element_](/ "CSS element 选择器") | p | 选择所有 \<p> 元素。 |
| [_element_._class_](/ "CSS element.class 选择器") | p.intro | 选择 class="intro" 的所有 \<p> 元素。 |
| [_element_,_element_](/ "CSS element,element 选择器") | div, p | 选择所有 \<div> 元素和所有 \<p> 元素。 |
| [_element_ _element_](/ "CSS element element 选择器") | div p | 选择 \<div> 元素内的所有 \<p> 元素。 |
| [_element_\>_element_](/ "CSS element>element 选择器") | div > p | 选择父元素是 \<div> 的所有 \<p> 元素。 |
| [_element_+_element_](/ "CSS element+element 选择器") | div + p | 选择紧跟 \<div> 元素的首个 \<p> 元素。 |
| [_element1_\~_element2_](/ "CSS element1~element2 选择器") | p \~ ul | 选择前面有 \<p> 元素的每个 \<ul> 元素。 |
| [\[_attribute_\]](/ "CSS [attribute] 选择器") | \[target\] | 选择带有 target 属性的所有元素。 |
| [\[_attribute_\=_value_\]](/ "CSS [attribute=value] 选择器") | \[target=\_blank\] | 选择带有 target="\_blank" 属性的所有元素。 |
| [\[_attribute_\~=_value_\]](/ "CSS [attribute~=value] 选择器") | \[title\~=flower\] | 选择 title 属性包含单词 "flower" 的所有元素。 |
| [\[_attribute_\|=_value_\]](/ "CSS [attribute\|=value] 选择器") | \[lang\|=en\] | 选择 lang 属性值以 "en" 开头的所有元素。 |
| [\[_attribute_\^=_value_\]](/ "CSS [attribute^=value] 选择器") | a\[href\^="https"\] | 选择其 src 属性值以 "https" 开头的每个 \<a> 元素。 |
| [\[_attribute_\$=_value_\]](/ "CSS [attribute$=value] 选择器") | a\[href\$=".pdf"\] | 选择其 src 属性以 ".pdf" 结尾的所有 \<a> 元素。 |
| [\[_attribute_\*=_value_\]](/ "CSS [attribute*=value] 选择器") | a\[href\*="w3schools"\] | 选择其 href 属性值中包含 "abc" 子串的每个 \<a> 元素。 |
| [:active](/ "CSS :active 选择器") | a:active | 选择活动链接。 |
| [::after](/ "CSS ::after 选择器") | p::after | 在每个 \<p> 的内容之后插入内容。 |
| [::before](/ "CSS ::before 选择器") | p::before | 在每个 \<p> 的内容之前插入内容。 |
| [:checked](/ "CSS :checked 选择器") | input:checked | 选择每个被选中的 \<input> 元素。 |
| [:default](/ "CSS :default 选择器") | input:default | 选择默认的 \<input> 元素。 |
| [:disabled](/ "CSS :disabled 选择器") | input:disabled | 选择每个被禁用的 \<input> 元素。 |
| [:empty](/ "CSS :empty 选择器") | p:empty | 选择没有子元素的每个 \<p> 元素（包括文本节点）。 |
| [:enabled](/ "CSS :enabled 选择器") | input:enabled | 选择每个启用的 \<input> 元素。 |
| [:first-child](/ "CSS :first-child 选择器") | p:first-child | 选择属于父元素的第一个子元素的每个 \<p> 元素。 |
| [::first-letter](/ "CSS ::first-letter 选择器") | p::first-letter | 选择每个 \<p> 元素的首字母。 |
| [::first-line](/ "CSS ::first-line 选择器") | p::first-line | 选择每个 \<p> 元素的首行。 |
| [:first-of-type](/ "CSS :first-of-type 选择器") | p:first-of-type | 选择属于其父元素的首个 \<p> 元素的每个 \<p> 元素。 |
| [:focus](/ "CSS :focus 选择器") | input:focus | 选择获得焦点的 input 元素。 |
| [:fullscreen](/ "CSS :fullscreen 选择器") | :fullscreen | 选择处于全屏模式的元素。 |
| [:hover](/ "CSS :hover 选择器") | a:hover | 选择鼠标指针位于其上的链接。 |
| [:in-range](/ "CSS :in-range 选择器") | input:in-range | 选择其值在指定范围内的 input 元素。 |
| [:indeterminate](/ "CSS :indeterminate 选择器") | input:indeterminate | 选择处于不确定状态的 input 元素。 |
| [:invalid](/ "CSS :invalid 选择器") | input:invalid | 选择具有无效值的所有 input 元素。 |
| [:lang\(_language_\)](/ "CSS :lang(language) 选择器") | p:lang\(it\) | 选择 lang 属性等于 "it"（意大利）的每个 \<p> 元素。 |
| [:last-child](/ "CSS :last-child 选择器") | p:last-child | 选择属于其父元素最后一个子元素每个 \<p> 元素。 |
| [:last-of-type](/ "CSS :last-of-type 选择器") | p:last-of-type | 选择属于其父元素的最后 \<p> 元素的每个 \<p> 元素。 |
| [:link](/ "CSS :link 选择器") | a:link | 选择所有未访问过的链接。 |
| [:not\(_selector_\)](/ "CSS :not(selector) 选择器") | :not\(p\) | 选择非 \<p> 元素的每个元素。 |
| [:nth-child\(_n_\)](/ "CSS :nth-child(n) 选择器") | p:nth-child\(2\) | 选择属于其父元素的第二个子元素的每个 \<p> 元素。 |
| [:nth-last-child\(_n_\)](/ "CSS :nth-last-child(n) 选择器") | p:nth-last-child\(2\) | 同上，从最后一个子元素开始计数。 |
| [:nth-of-type\(_n_\)](/ "CSS :nth-of-type(n) 选择器") | p:nth-of-type\(2\) | 选择属于其父元素第二个 \<p> 元素的每个 \<p> 元素。 |
| [:nth-last-of-type\(_n_\)](/ "CSS :nth-last-of-type(n) 选择器") | p:nth-last-of-type\(2\) | 同上，但是从最后一个子元素开始计数。 |
| [:only-of-type](/ "CSS :only-of-type 选择器") | p:only-of-type | 选择属于其父元素唯一的 \<p> 元素的每个 \<p> 元素。 |
| [:only-child](/ "CSS :only-child 选择器") | p:only-child | 选择属于其父元素的唯一子元素的每个 \<p> 元素。 |
| [:optional](/ "CSS :optional 选择器") | input:optional | 选择不带 "required" 属性的 input 元素。 |
| [:out-of-range](/ "CSS :out-of-range 选择器") | input:out-of-range | 选择值超出指定范围的 input 元素。 |
| [::placeholder](/ "CSS ::placeholder 选择器") | input::placeholder | 选择已规定 "placeholder" 属性的 input 元素。 |
| [:read-only](/ "CSS :read-only 选择器") | input:read-only | 选择已规定 "readonly" 属性的 input 元素。 |
| [:read-write](/ "CSS :read-write 选择器") | input:read-write | 选择未规定 "readonly" 属性的 input 元素。 |
| [:required](/ "CSS :required 选择器") | input:required | 选择已规定 "required" 属性的 input 元素。 |
| [:root](/ "CSS :root 选择器") | :root | 选择文档的根元素。 |
| [::selection](/ "CSS ::selection 选择器") | ::selection | 选择用户已选取的元素部分。 |
| [:target](/ "CSS :target 选择器") | #news:target | 选择当前活动的 #news 元素。 |
| [:valid](/ "CSS :valid 选择器") | input:valid | 选择带有有效值的所有 input 元素。 |
| [:visited](/ "CSS :visited 选择器") | a:visited | 选择所有已访问的链接。 |