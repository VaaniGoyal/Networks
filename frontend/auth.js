import axios from "axios";

const API_URL = "http://backend_ip:8000";

export const register = async (username, password) => {
    return axios.post(`${API_URL}/auth/register`, { username, password });
};

export const login = async (username, password) => {
    return axios.post(`${API_URL}/auth/login`, { username, password });
};
