import React from "react";

export default function ResultTable({ rows }) {
  if (!rows || rows.length === 0) return null;

  return (
    <div className="mt-6 overflow-x-auto">
      <table className="min-w-full bg-slate-800 rounded-lg">
        <thead>
          <tr>
            {Object.keys(rows[0]).map((col) => (
              <th
                key={col}
                className="px-4 py-2 border-b border-gray-700 text-left text-sm text-gray-300"
              >
                {col}
              </th>
            ))}
          </tr>
        </thead>

        <tbody>
          {rows.map((row, idx) => (
            <tr key={idx} className="hover:bg-slate-700">
              {Object.values(row).map((v, i) => (
                <td
                  key={i}
                  className="px-4 py-2 text-sm border-b border-gray-800 text-gray-200"
                >
                  {v}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}