from .byzantium import Byzantium
from opcodes.opcode import Opcode


class Constantinople(Byzantium):
    STOP = Byzantium.STOP
    ADD = Byzantium.ADD
    MUL = Byzantium.MUL
    SUB = Byzantium.SUB
    DIV = Byzantium.DIV
    SDIV = Byzantium.SDIV
    MOD = Byzantium.MOD
    SMOD = Byzantium.SMOD
    ADDMOD = Byzantium.ADDMOD
    MULMOD = Byzantium.MULMOD
    EXP = Byzantium.EXP
    SIGNEXTEND = Byzantium.SIGNEXTEND
    LT = Byzantium.LT
    GT = Byzantium.GT
    SLT = Byzantium.SLT
    SGT = Byzantium.SGT
    EQ = Byzantium.EQ
    ISZERO = Byzantium.ISZERO
    AND = Byzantium.AND
    OR = Byzantium.OR
    XOR = Byzantium.XOR
    NOT = Byzantium.NOT
    BYTE = Byzantium.BYTE
    SHA3 = Byzantium.SHA3
    ADDRESS = Byzantium.ADDRESS
    BALANCE = Byzantium.BALANCE
    ORIGIN = Byzantium.ORIGIN
    CALLER = Byzantium.CALLER
    CALLVALUE = Byzantium.CALLVALUE
    CALLDATALOAD = Byzantium.CALLDATALOAD
    CALLDATASIZE = Byzantium.CALLDATASIZE
    CALLDATACOPY = Byzantium.CALLDATACOPY
    CODESIZE = Byzantium.CODESIZE
    CODECOPY = Byzantium.CODECOPY
    GASPRICE = Byzantium.GASPRICE
    EXTCODESIZE = Byzantium.EXTCODESIZE
    EXTCODECOPY = Byzantium.EXTCODECOPY
    BLOCKHASH = Byzantium.BLOCKHASH
    COINBASE = Byzantium.COINBASE
    TIMESTAMP = Byzantium.TIMESTAMP
    NUMBER = Byzantium.NUMBER
    DIFFICULTY = Byzantium.DIFFICULTY
    GASLIMIT = Byzantium.GASLIMIT
    POP = Byzantium.POP
    MLOAD = Byzantium.MLOAD
    MSTORE = Byzantium.MSTORE
    MSTORE8 = Byzantium.MSTORE8
    SLOAD = Byzantium.SLOAD
    SSTORE = Byzantium.SSTORE
    JUMP = Byzantium.JUMP
    JUMPI = Byzantium.JUMPI
    PC = Byzantium.PC
    MSIZE = Byzantium.MSIZE
    GAS = Byzantium.GAS
    JUMPDEST = Byzantium.JUMPDEST
    PUSH1 = Byzantium.PUSH1
    PUSH2 = Byzantium.PUSH2
    PUSH3 = Byzantium.PUSH3
    PUSH4 = Byzantium.PUSH4
    PUSH5 = Byzantium.PUSH5
    PUSH6 = Byzantium.PUSH6
    PUSH7 = Byzantium.PUSH7
    PUSH8 = Byzantium.PUSH8
    PUSH9 = Byzantium.PUSH9
    PUSH10 = Byzantium.PUSH10
    PUSH11 = Byzantium.PUSH11
    PUSH12 = Byzantium.PUSH12
    PUSH13 = Byzantium.PUSH13
    PUSH14 = Byzantium.PUSH14
    PUSH15 = Byzantium.PUSH15
    PUSH16 = Byzantium.PUSH16
    PUSH17 = Byzantium.PUSH17
    PUSH18 = Byzantium.PUSH18
    PUSH19 = Byzantium.PUSH19
    PUSH20 = Byzantium.PUSH20
    PUSH21 = Byzantium.PUSH21
    PUSH22 = Byzantium.PUSH22
    PUSH23 = Byzantium.PUSH23
    PUSH24 = Byzantium.PUSH24
    PUSH25 = Byzantium.PUSH25
    PUSH26 = Byzantium.PUSH26
    PUSH27 = Byzantium.PUSH27
    PUSH28 = Byzantium.PUSH28
    PUSH29 = Byzantium.PUSH29
    PUSH30 = Byzantium.PUSH30
    PUSH31 = Byzantium.PUSH31
    PUSH32 = Byzantium.PUSH32
    DUP1 = Byzantium.DUP1
    DUP2 = Byzantium.DUP2
    DUP3 = Byzantium.DUP3
    DUP4 = Byzantium.DUP4
    DUP5 = Byzantium.DUP5
    DUP6 = Byzantium.DUP6
    DUP7 = Byzantium.DUP7
    DUP8 = Byzantium.DUP8
    DUP9 = Byzantium.DUP9
    DUP10 = Byzantium.DUP10
    DUP11 = Byzantium.DUP11
    DUP12 = Byzantium.DUP12
    DUP13 = Byzantium.DUP13
    DUP14 = Byzantium.DUP14
    DUP15 = Byzantium.DUP15
    DUP16 = Byzantium.DUP16
    SWAP1 = Byzantium.SWAP1
    SWAP2 = Byzantium.SWAP2
    SWAP3 = Byzantium.SWAP3
    SWAP4 = Byzantium.SWAP4
    SWAP5 = Byzantium.SWAP5
    SWAP6 = Byzantium.SWAP6
    SWAP7 = Byzantium.SWAP7
    SWAP8 = Byzantium.SWAP8
    SWAP9 = Byzantium.SWAP9
    SWAP10 = Byzantium.SWAP10
    SWAP11 = Byzantium.SWAP11
    SWAP12 = Byzantium.SWAP12
    SWAP13 = Byzantium.SWAP13
    SWAP14 = Byzantium.SWAP14
    SWAP15 = Byzantium.SWAP15
    SWAP16 = Byzantium.SWAP16
    LOG0 = Byzantium.LOG0
    LOG1 = Byzantium.LOG1
    LOG2 = Byzantium.LOG2
    LOG3 = Byzantium.LOG3
    LOG4 = Byzantium.LOG4
    CREATE = Byzantium.CREATE
    CALL = Byzantium.CALL
    CALLCODE = Byzantium.CALLCODE
    RETURN = Byzantium.RETURN
    SELFDESTRUCT = Byzantium.SELFDESTRUCT
    DELEGATECALL = Byzantium.DELEGATECALL
    REVERT = Byzantium.REVERT
    RETURNDATASIZE = Byzantium.RETURNDATASIZE
    RETURNDATACOPY = Byzantium.RETURNDATACOPY
    STATICCALL = Byzantium.STATICCALL
    SHL = Opcode("SHL", 3, 0x1B)
    SHR = Opcode("SHR", 3, 0x1C)
    SAR = Opcode("SAR", 3, 0x1D)
    EXTCODEHASH = Opcode("EXTCODEHASH", 400, 0x3F)
    CREATE2 = Opcode("CREATE2", 32000, 0xF5)
