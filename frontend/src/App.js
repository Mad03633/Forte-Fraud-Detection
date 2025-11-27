import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import ResultTable from "./components/ResultTable";
import { sendForPrediction, retrainModel } from "./api";

function App() {
  const [predictionFile, setPredictionFile] = useState(null);
  const [retrainFile, setRetrainFile] = useState(null);
  const [results, setResults] = useState([]);

  async function handlePredict() {
    if (!predictionFile) return;
    const data = await sendForPrediction(predictionFile);
    setResults(data.rows);
  }

  async function handleRetrain() {
    if (!retrainFile) return;
    await retrainModel(retrainFile);
    alert("Model retrained successfully!");
  }

  return (
    <div className="min-h-screen bg-[#0A0F24] text-white px-6 py-10">
      
      {/* Header */}
      <div className="text-center mb-12">
        <h1 className="text-4xl font-extrabold tracking-wide">
          ForteBank Fraud Detection MVP
        </h1>
        <div className="mx-auto mt-3 w-48 h-1 bg-blue-500 rounded-full"></div>
      </div>

      {/* Container */}
      <div className="max-w-3xl mx-auto space-y-12">

        {/* PREDICT BLOCK */}
        <div className="backdrop-blur-md bg-white/5 border border-white/10 shadow-xl rounded-2xl p-8">
          <h2 className="text-2xl font-semibold mb-4">Upload CSV for prediction</h2>

          <FileUpload onFileSelected={setPredictionFile} title="" />

          <button
            onClick={handlePredict}
            className="mt-6 w-full py-3 bg-gradient-to-r from-blue-500 to-blue-700 hover:from-blue-600 hover:to-blue-800 font-medium rounded-xl shadow-lg transition"
          >
            Predict
          </button>
        </div>

        {/* RETRAIN BLOCK */}
        <div className="backdrop-blur-md bg-white/5 border border-white/10 shadow-xl rounded-2xl p-8">
          <h2 className="text-2xl font-semibold mb-4">CSV for retraining the model</h2>

          <FileUpload onFileSelected={setRetrainFile} title="" />

          <button
            onClick={handleRetrain}
            className="mt-6 w-full py-3 bg-gradient-to-r from-amber-500 to-orange-600 hover:from-amber-600 hover:to-orange-700 font-medium rounded-xl shadow-lg transition"
          >
            Retrain the model
          </button>
        </div>

        {/* RESULTS */}
        <ResultTable rows={results} />
      </div>
    </div>
  );
}

export default App;