import tags from "../data/tags.json";
import "./TagList.css";

function TagList({ addTag }) {
  const coloring = ['red', 'blue', 'pink', 'green'];

  function handleTagClick(name) {
    addTag(name); // agora adiciona ao array de tags
  }

  return (
    <div className="tagContainer">
      <ul className="tagList">
        {tags.map((tag, index) => (
          <li 
            className={`tagEl ${coloring[index % coloring.length]}`} 
            key={tag.id}
          >
            <button
              className="tagBtn"
              onClick={() => handleTagClick(tag.name)}
            >
              {tag.name}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TagList;
