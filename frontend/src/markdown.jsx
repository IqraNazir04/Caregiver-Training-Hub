import React from "react";

export function renderInline(text, keyPrefix) {
  return text.split(/(\*\*.+?\*\*|\*.+?\*)/g).map((part, i) => {
    if (part.startsWith("**") && part.endsWith("**")) {
      return <strong key={`${keyPrefix}-${i}`}>{part.slice(2, -2)}</strong>;
    }
    if (part.startsWith("*") && part.endsWith("*")) {
      return <em key={`${keyPrefix}-${i}`}>{part.slice(1, -1)}</em>;
    }
    return part;
  });
}

export function renderMarkdown(text) {
  const blocks = [];
  let list = null;

  text.split("\n").forEach((rawLine) => {
    const line = rawLine.trim();
    if (!line) {
      return;
    }
    const bullet = line.match(/^[-*]\s+(.*)/);
    if (bullet) {
      if (!list) {
        list = { type: "ul", items: [] };
        blocks.push(list);
      }
      list.items.push(bullet[1]);
      return;
    }
    list = null;
    if (line.startsWith("## ")) {
      blocks.push({ type: "h4", text: line.slice(3) });
    } else {
      blocks.push({ type: "p", text: line });
    }
  });

  return blocks.map((block, i) => {
    if (block.type === "ul") {
      return (
        <ul key={i}>
          {block.items.map((item, j) => (
            <li key={j}>{renderInline(item, `${i}-${j}`)}</li>
          ))}
        </ul>
      );
    }
    if (block.type === "h4") {
      return <h4 key={i}>{renderInline(block.text, `${i}`)}</h4>;
    }
    return <p key={i}>{renderInline(block.text, `${i}`)}</p>;
  });
}
