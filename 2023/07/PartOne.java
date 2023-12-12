package day7;

import utilities.Input;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class PartOne {
    private class Hand {
        String hand;
        Map<Character, Integer> handMap;
        int type;
        public Hand(String hand) {
            this.hand = hand;
            handMap = new HashMap<>();
            for (char c : hand.toCharArray()) {
                handMap.put(c, handMap.getOrDefault(c, 0) + 1);
            }
            if (isFiveOfAKind()) type = 6;
            else if (isFourOfAKind()) type = 5;
            else if (isFullHouse()) type = 4;
            else if (isThreeOfAKind()) type = 3;
            else if (isTwoPair()) type = 2;
            else if (isOnePair()) type = 1;
            else type = 0;
        }
        public int mapCardToValue(char c) {
            return switch (c) {
                case 'A' -> 14;
                case 'K' -> 13;
                case 'Q' -> 12;
                case 'J' -> 11;
                case 'T' -> 10;
                default -> Character.getNumericValue(c);
            };
        }
        public int compareByCard(Hand other) {
            char[] thisHand = hand.toCharArray();
            char[] otherHand = other.hand.toCharArray();
            for (int i = 0; i < thisHand.length; i++) {
                if (mapCardToValue(thisHand[i]) > mapCardToValue(otherHand[i])) {
                    return 1;
                } else if (mapCardToValue(thisHand[i]) < mapCardToValue(otherHand[i])) {
                    return -1;
                }
            }
            return 0;
        }
        private boolean isFiveOfAKind() {
            return handMap.size() == 1;
        }
        private boolean isFourOfAKind() {
            return handMap.containsValue(4);
        }
        private boolean isFullHouse() {
            return handMap.containsValue(3) && handMap.containsValue(2);
        }
        private boolean isThreeOfAKind() {
            return handMap.containsValue(3);
        }
        public boolean isTwoPair() {
            ArrayList<Integer> values = new ArrayList<>(handMap.values());
            values.removeIf(value -> value == 2);
            return values.size() == 1;
        }
        private boolean isOnePair() {
            return handMap.containsValue(2);
        }

        public int compareTo(Hand other) {
            if (this.type > other.type) return 1;
            else if (this.type < other.type) return -1;
            else return compareByCard(other);
        }
    }

    public static void main(String[] args) {
        PartOne p1 = new PartOne();
        String[] input = Input.readInput("day7/input.txt");
        Map<Hand, Integer> bets = new HashMap<>();
        for (String line : input) {
            String[] split = line.split(" ");
            bets.put(p1.new Hand(split[0]), Integer.parseInt(split[1]));
        }
        ArrayList<Hand> ranks = new ArrayList<>(bets.keySet());
        ranks.sort(Hand::compareTo);
        int solution = 0;
        for (int i = 0; i < ranks.size(); i++) {
            System.out.println(ranks.get(i).hand);
            solution += bets.get(ranks.get(i)) * (i+1);
        }
        System.out.println(solution);
    }
}
