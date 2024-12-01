import axios from "axios";

const API_URL = "http://backend_ip:8000";

export const uploadFile = async (file, category) => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("category", category);
    return axios.post(`${API_URL}/files/upload`, formData);
};

export const listFiles = async (category) => {
    return axios.get(`${API_URL}/files`, { params: { category } });
};

export const searchFiles = async (filename) => {
    return axios.get(`${API_URL}/files/search`, { params: { filename } });
};
