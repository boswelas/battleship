
const horizontalAxis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
const verticalAxis = ['0', '1', '2', '3', '4', '5', '6', '7']

export default function PlayerBoard() {
    let board = []
    for (let j = 0; j < verticalAxis.length; j++) {
        for (let i = 0; i < horizontalAxis.length; i++) {
            const coord = `${horizontalAxis[i]}${verticalAxis[j]}`;
            board.push(
                <div key={coord} className="border border-gray-600 flex items-center justify-center h-full w-full">
                    {coord}
                </div>
            );
        }
    }
    return (
        <div>
            <div className="bg-blue-400 h-96 w-96 grid grid-cols-8 grid-rows-8 ">
                {board}
            </div>
        </div>
    )
}
