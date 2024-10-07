import React, { useState } from "react";
import { postData } from "../api/apiService";

const PostDataForm = () => {
  const [inputValue, setInputValue] = useState("");
  const [responseMessage, setResponseMessage] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const data = { message: inputValue };
      const url = "http://localhost:9090/make_post";
      const response = await postData(url, data);
      setResponseMessage(response);
      setError(null);
    } catch (err) {
      setError(err.message);
      setResponseMessage(null);
    }
  };

  return (
    <div>
      <h2>Send Data to API</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Enter Message:
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Type your message here!"
          />
        </label>
        <button type="submit">Submit</button>
      </form>

      {responseMessage && (
        <div>
          <h3>Response from API:</h3>
          <pre>{JSON.stringify(responseMessage, null, 2)}</pre>
        </div>
      )}

      {error && (
        <div>
          <h3>Error:</h3>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
};

export default PostDataForm;
