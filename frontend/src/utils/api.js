import { useAuth } from "@clerk/clerk-react";
import { useCallback } from "react";

export const useApi = () => {
  const { getToken } = useAuth();

  const makeRequest = useCallback(async (endpoint, options = {}) => {
    const token = await getToken();
    const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';
    const defaultOptions = {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
    };

    const response = await fetch(`${API_URL}/${endpoint}`, {
      ...defaultOptions,
      ...options,
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => null);
      if (response.status === 429) {
        throw new Error("Daily quota exceeded");
      }
      throw new Error(errorData?.detail || "An error occurred");
    }

    return response.json();
  }, [getToken]);

  return { makeRequest };
};
