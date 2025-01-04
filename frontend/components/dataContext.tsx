"use client";
import { createContext, useContext, useState,ReactNode } from 'react';

const DataContext = createContext<any>(null);

export const DataProvider = ({ children }: { children: ReactNode }) => {
  const [username,setUsername] = useState({
    username: "",
  });

  return (
    <DataContext.Provider value={{ username,setUsername }}>
      {children}
    </DataContext.Provider>
  );
};

export const useData = () => useContext(DataContext);
