import React from "react";
import { useState, useEffect } from "react";
import MCQChallenge from "../challenge/MCQChallenge";
import { useApi } from "../utils/api";

const HistoryPanel = () => {
  const [history, setHistory] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const { makeRequest } = useApi();

  const fetchHistory = React.useCallback(async () => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await makeRequest("my-history");
      setHistory(response.challenges);
    } catch (error) {
      setError(error.message);
    } finally {
      setIsLoading(false);
    }
  }, [makeRequest]);

  useEffect(() => {
    fetchHistory();
  }, [fetchHistory]);


  if (isLoading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return (
      <div className="error-message">
        <p>{error}</p> <button onClick={fetchHistory}>Retry</button>
      </div>
    );
  }

  return (
    <div className="history-panel">
      <h2>History</h2>
      {history.length === 0 ? (
        <p>No history available</p>
      ) : (
        <div className="history-list">
          {history.slice().reverse().map((challenge, index) => (
            <MCQChallenge
              key={index}
              challenge={challenge}
              showExplanation={false}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default HistoryPanel;
