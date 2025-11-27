import React, { useState } from "react";

export default function FileUpload({ onFileSelected }) {
  const [file, setFile] = useState(null);

  function handleSelect(e) {
    const f = e.target.files[0];
    setFile(f);
    onFileSelected(f);
  }

  return (
    <div>
      <label className="block w-full cursor-pointer">
        <div className="bg-slate-800/60 border border-slate-700 rounded-xl px-4 py-3 text-gray-300 hover:bg-slate-800 transition">
          <span className="font-medium">
            {file ? file.name : "Choose CSV file"}
          </span>
        </div>

        <input
          type="file"
          accept=".csv"
          onChange={handleSelect}
          className="hidden"
        />
      </label>
    </div>
  );
}