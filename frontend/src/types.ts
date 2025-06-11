export interface GameProfile {
    name: string;
}

export interface Command {
    command: "start_auto" | "stop_auto" | "execute";
    params?: {
        task?: string;
        preset?: string;
        x?: number;
        y?: number;
        [key: string]: any;
    };
}