import Image from "next/image";
import PlayerBoard from "./components/PlayerBoard";

export default function Home() {
  return (
    <div>
      <div>
        <h1>Battleship</h1>
      </div>
      <div>
        <PlayerBoard />
      </div>

    </div>
  );
}
