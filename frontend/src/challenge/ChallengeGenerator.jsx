import React from "react";
import { useState, useEffect, useCallback } from "react";
import MCQChallenge from "./MCQChallenge";
import { useApi } from "../utils/api";

const ChallengeGenerator = () => {
  const [challenge, setChallenge] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [difficulty, setDifficulty] = useState("easy");
  const [quota, setQuota] = useState(0);
  const { makeRequest } = useApi();

  const fetchQuota = useCallback(async () => {
    try {
      const response = await makeRequest("quota");
      setQuota(response);
    } catch (error) {
      setError(error.message);
    }
  }, [makeRequest]);

  useEffect(() => {
    fetchQuota();
  }, [fetchQuota]);

  const generateChallenge = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await makeRequest("generate-challenge", {
        method: "POST",
        body: JSON.stringify({ difficulty }),
      });
      setChallenge(response);
      fetchQuota();
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  const getNextResetTime = () => {
    if (!quota?.last_reset_date) return null;
    try {
      const resetDate = new Date(quota.last_reset_date);
      resetDate.setHours(resetDate.getHours() + 24);
      return resetDate;
    } catch (e) {
      console.error('Error parsing reset date:', e);
      return null;
    }
  };

  return (
    <div className="challenge-container">
      <h2>Coding Challenge Generator</h2>
      <div className="quota-display">
        <p>Challenges Remaining: {quota?.quota_remaining ?? 'Loading...'}</p>
        {quota?.quota_remaining === 0 && getNextResetTime() && (
          <p>Reset at: {getNextResetTime().toLocaleString()}</p>
        )}
      </div>
      <div className="difficulty-selector">
        <label htmlFor="difficulty"> Select Difficulty:</label>
        <select
          id="difficulty"
          value={difficulty}
          onChange={(e) => setDifficulty(e.target.value)}
          disabled={loading}
        >
          <option value="easy">Easy</option>
          <option value="medium">Medium</option>
          <option value="hard">Hard</option>
        </select>
      </div>
      <button
        className="generate-button"
        onClick={generateChallenge}
        disabled={loading || quota?.quota_remaining === 0}
      >
        {loading ? "Generating..." : "Generate Challenge"}
      </button>
      {error && <p className="error-message">{error}</p>}
      {challenge && <MCQChallenge challenge={challenge} />}
    </div>
  );
};

export default ChallengeGenerator;
