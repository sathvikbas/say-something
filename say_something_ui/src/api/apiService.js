import axios from "axios";

export const postData = async (url, data) => {
  try {
    console.log("DATA: ", data);
    const response = await axios.post(url, data);
    return response.data;
  } catch (error) {
    throw new Error(`Error posting data: ${error.message}`);
  }
};
